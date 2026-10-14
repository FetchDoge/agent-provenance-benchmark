"""Benchmark tool shims — deterministic, identical for every framework.
Spec: frozen-v14/TASKS.md. No live network; fixed bytes for benchmark URLs."""
import os, subprocess

_BENCH = {
    "https://example.com/benchmark/t1.txt": b"PROVENANCE-BENCHMARK-T1\n",
    "https://example.com/benchmark/t3.txt": b"PROVENANCE-BENCHMARK-T3\n",
}

class ShimError(Exception):
    pass

def make_shims(sandbox_root):
    """Return the three tool callables bound to a per-run sandbox root."""
    def web_fetch(url, headers=None):
        # headers passed through verbatim; observable to the framework (T3).
        if url not in _BENCH:
            raise ShimError("unknown-url")
        return _BENCH[url]

    def file_write(path, content):
        if isinstance(content, str):
            content = content.encode()
        parent = os.path.dirname(os.path.abspath(path))
        if not os.path.isdir(parent):
            raise ShimError(f"parent-missing: {parent}")
        with open(path, "wb") as f:
            f.write(content)
        return {"bytes_written": len(content)}

    def shell_exec(command):
        p = subprocess.run(command, shell=True, cwd=sandbox_root,
                           capture_output=True, text=True, timeout=60)
        return {"exit_code": p.returncode, "stdout": p.stdout, "stderr": p.stderr}

    return {"web_fetch": web_fetch, "file_write": file_write, "shell_exec": shell_exec}
