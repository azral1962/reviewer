#!/usr/bin/env python3
"""Validate repository/cycle integrity; does not certify competence."""
import csv,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]; errors=[]
def need(p):
    if not (root/p).is_file(): errors.append(f"Missing {p}")
for p in ['AGENTS.md','README.md','master/MASTER.md','master/version.json','master/CHANGELOG.md','knowledge/SOURCES.csv','prompts/teacher.md','prompts/learner.md','prompts/examiner.md','prompts/reconcile.md']:
    need(p)
def load(p):
    try:return json.loads(p.read_text())
    except (ValueError,OSError) as e: errors.append(f"Invalid JSON {p.relative_to(root)}: {e}"); return {}
v=load(root/'master/version.json')
if not re.fullmatch(r"\d+\.\d+\.\d+",str(v.get('version',''))): errors.append('Invalid Master version')
source_ids=set()
try:
    with (root/'knowledge/SOURCES.csv').open(newline='') as f:
        reader=csv.DictReader(f)
        if reader.fieldnames!=['source_id','kind','title','authority','version','location','retrieved_on','access_status']: errors.append('Invalid source registry header')
        for row in reader:
            sid=row['source_id']
            if not sid or sid in source_ids: errors.append(f'Empty/duplicate source ID: {sid}')
            source_ids.add(sid)
except OSError as e: errors.append(str(e))
closed={}
for cycle in sorted((root/'cycles').iterdir()):
    if not cycle.is_dir(): continue
    m=load(cycle/'manifest.json'); rel=cycle.relative_to(root)
    if m.get('cycle_id')!=cycle.name: errors.append(f'{rel}: cycle ID mismatch')
    if m.get('status') not in ['draft','taught','executed','examined','closed']: errors.append(f'{rel}: invalid status')
    if not re.fullmatch(r"\d+\.\d+\.\d+",str(m.get('master_before',''))): errors.append(f'{rel}: invalid starting version')
    for sid in m.get('sources',[]):
        if sid not in source_ids: errors.append(f'{rel}: unknown source {sid}')
    for p in ['teaching-package.md','assessment-specification.md','result.md','evidence.csv','examination.md','update-proposal.md','decision.md']: need(str(rel/p))
    if m.get('status')=='closed':
        after=m.get('master_after',''); before=m.get('master_before','')
        if not re.fullmatch(r"\d+\.\d+\.\d+",str(after)) or tuple(map(int,after.split('.')))<=tuple(map(int,before.split('.'))): errors.append(f'{rel}: closing version must advance')
        else: closed[cycle.name]=after
        for p in ['teaching-package.md','assessment-specification.md','result.md','examination.md','update-proposal.md','decision.md']:
            path=cycle/p
            if path.exists() and re.search(r'\bTODO\b|awaiting human decision',path.read_text(),re.I): errors.append(f'{rel}/{p}: unfinished closed record')
        if cycle.name not in (root/'master/CHANGELOG.md').read_text(): errors.append(f'{rel}: missing changelog entry')
latest=v.get('latest_cycle')
if latest is not None and (latest not in closed or closed[latest]!=v.get('version')): errors.append('Latest cycle must be closed and match Master version')
if errors:
    print('Validation failed:\n'+'\n'.join('- '+e for e in errors)); sys.exit(1)
print('PASS: repository structure and cycle integrity. Domain judgments require examination.')
