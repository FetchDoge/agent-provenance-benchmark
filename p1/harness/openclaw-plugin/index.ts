import { execFile } from "node:child_process";
import { Type } from "typebox";
import { defineToolPlugin } from "openclaw/plugin-sdk/tool-plugin";

// Benchmark harness shims for OpenClaw. Each tool delegates to the frozen
// Python shim implementations (harness/shims.py) through a one-shot bridge
// process, so behavior is byte-identical to every other framework's tools.
// The per-run sandbox root arrives via plugin config (sandboxDir).

const BRIDGE = new URL("../openclaw-shim-bridge.py", import.meta.url).pathname;

type ShimResult = { ok: boolean; text?: string; error?: string };

function callShim(
  tool: string,
  args: Record<string, unknown>,
  sandboxDir: string,
): Promise<ShimResult> {
  return new Promise((resolve, reject) => {
    const child = execFile(
      "python3",
      [BRIDGE, tool],
      { env: { ...process.env, SHIM_SANDBOX: sandboxDir } },
      (err, stdout) => {
        if (err) {
          reject(err);
          return;
        }
        try {
          resolve(JSON.parse(stdout) as ShimResult);
        } catch (e) {
          reject(e as Error);
        }
      },
    );
    child.stdin?.end(JSON.stringify(args));
  });
}

export default defineToolPlugin({
  id: "harness-shims",
  name: "Harness Shims",
  description: "Benchmark harness tool shims (frozen TASKS.md behavior).",
  configSchema: Type.Object({
    sandboxDir: Type.String({ description: "Per-run sandbox root directory." }),
  }),
  tools: (tool) => [
    tool({
      name: "web_fetch",
      label: "Web Fetch",
      description: "Fetch a URL and return its text.",
      parameters: Type.Object({
        url: Type.String({ description: "The URL to fetch." }),
        headers: Type.Optional(
          Type.Record(Type.String(), Type.String(), {
            description: "Optional HTTP headers to send verbatim.",
          }),
        ),
      }),
      execute: async (args, config) => {
        const r = await callShim("web_fetch", { ...args }, config.sandboxDir);
        if (!r.ok) throw new Error(r.error ?? "web_fetch failed");
        return r.text ?? "";
      },
    }),
    tool({
      name: "file_write",
      label: "File Write",
      description: "Write content to a file path in the working directory.",
      parameters: Type.Object({
        path: Type.String({ description: "File path, relative to the working directory or absolute." }),
        content: Type.String({ description: "The content to write." }),
      }),
      execute: async (args, config) => {
        const r = await callShim("file_write", { ...args }, config.sandboxDir);
        if (!r.ok) throw new Error(r.error ?? "file_write failed");
        return r.text ?? "";
      },
    }),
    tool({
      name: "shell_exec",
      label: "Shell Exec",
      description: "Run a shell command in the working directory.",
      parameters: Type.Object({
        command: Type.String({ description: "The shell command to run." }),
      }),
      execute: async (args, config) => {
        const r = await callShim("shell_exec", { ...args }, config.sandboxDir);
        if (!r.ok) throw new Error(r.error ?? "shell_exec failed");
        return r.text ?? "";
      },
    }),
  ],
});
