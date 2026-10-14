import subprocess, os, sys, json, time

CONN = '/home/hatch/workspace/custom-connectors/custom.legacy-grok'
P2 = '/home/hatch/workspace/portfolio-hackathon/phase3/p2'
SLUGS = ['langchain','deer-flow','hermes-agent','autogpt','metagpt','deepseek-harness',
         'gemini-cli','openhands','ruflo','openclaw']
env = dict(os.environ)
env['PYTHONPATH'] = '/opt/muse/skills/custom-connector-setup/bin'
os.makedirs(f'{P2}/lane-grok', exist_ok=True)
log = open(f'{P2}/lane-grok/driver.log', 'a')
for slug in SLUGS:
    out_path = f'{P2}/lane-grok/raw-{slug}.txt'
    if os.path.exists(out_path) and os.path.getsize(out_path) > 200:
        log.write(f'{slug}: already present, skipped\n'); log.flush(); continue
    pack = open(f'{P2}/packs/{slug}.md').read()
    t0 = time.time()
    try:
        r = subprocess.run(['python3', 'bin/grok.py', 'ask', '--bot', 'auditor', pack,
                            '--max-tokens', '2200'],
                           cwd=CONN, env=env, capture_output=True, text=True, timeout=600)
        with open(out_path, 'w') as f:
            f.write('=== STDOUT ===\n' + r.stdout + '\n=== STDERR ===\n' + r.stderr)
        log.write(f'{slug}: rc={r.returncode} bytes={len(r.stdout)} dur={time.time()-t0:.0f}s\n')
    except Exception as e:
        log.write(f'{slug}: EXCEPTION {e}\n')
    log.flush()
log.write('DRIVER DONE\n'); log.close()
print('driver done')
