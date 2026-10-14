import subprocess, os, time
CONN = '/home/hatch/workspace/custom-connectors/custom.legacy-grok'
P2 = '/home/hatch/workspace/portfolio-hackathon/phase3/p2'
env = dict(os.environ); env['PYTHONPATH'] = '/opt/muse/skills/custom-connector-setup/bin'
pack = open(f'{P2}/packs/langchain.md').read()
t0 = time.time()
r = subprocess.run(['python3','bin/grok.py','ask','--bot','auditor',pack,'--max-tokens','2200'],
                   cwd=CONN, env=env, capture_output=True, text=True, timeout=1700)
with open(f'{P2}/lane-grok/raw-langchain.txt','w') as f:
    f.write('=== STDOUT ===\n' + r.stdout + '\n=== STDERR ===\n' + r.stderr)
print(f'langchain retry: rc={r.returncode} bytes={len(r.stdout)} dur={time.time()-t0:.0f}s')
