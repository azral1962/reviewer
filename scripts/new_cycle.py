#!/usr/bin/env python3
import json,re,shutil,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
if len(sys.argv)!=2 or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}",sys.argv[1]):
    sys.exit("Usage: python3 scripts/new_cycle.py cycle-001 (lowercase ID)")
id=sys.argv[1]; dest=root/'cycles'/id
if dest.exists(): sys.exit("Cycle already exists; refusing overwrite")
v=json.loads((root/'master/version.json').read_text())['version']
commit=subprocess.run(['git','rev-parse','HEAD'],cwd=root,capture_output=True,text=True)
dest.mkdir()
manifest={'cycle_id':id,'status':'draft','master_before':v,'master_before_commit':commit.stdout.strip() if commit.returncode==0 else None,'master_after':None,'sources':[]}
(dest/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
for file in (root/'templates').iterdir():
    if file.is_file(): shutil.copyfile(file,dest/file.name)
print(dest)
