from pathlib import Path
import json,shutil,hashlib
import polars as pl
import numpy as np
from case_studies.utils.published_artifacts import publish_artifact,materialize_artifact,MANIFEST_NAME,file_sha256
src=Path('/Users/alex/workspaces/trading/.runtime/maintenance-2026-10-12/mlft-fixture/intermediates/nasdaq100_microstructure/features/financial.parquet')
root=Path('/Users/alex/workspaces/trading/.runtime/maintenance-2026-10-12/mlft-shards-controls')
root.mkdir(exist_ok=True)
public=root/'published'/'financial.parquet'
publish_artifact(src,public)
original=file_sha256(src)
record=json.loads((public/MANIFEST_NAME).read_text())
runtime=root/'runtime'/'financial.parquet'
runtime.parent.mkdir(exist_ok=True)
shutil.copytree(public,runtime)
materialize_artifact(runtime)
a,b=pl.read_parquet(src),pl.read_parquet(runtime)
results={'source_sha256':original,'runtime_sha256':file_sha256(runtime),'bytes_identical':original==file_sha256(runtime),'source_preserved':src.is_file() and file_sha256(src)==original,'rows':a.height,'schema_equal':a.schema==b.schema,'row_order_and_values_equal':a.equals(b),'float32_bits_equal':all(np.array_equal(a[c].to_numpy().view('uint32'),b[c].to_numpy().view('uint32')) for c,t in a.schema.items() if t==pl.Float32),'publication_manifest':record,'negative_controls':{}}
for kind in ('checksum','traversal','duplicate','symlink','canonical_checksum','unlisted','rows','schema'):
 path=root/kind/'financial.parquet'
 path.parent.mkdir(exist_ok=True)
 shutil.copytree(public,path)
 manifest=json.loads((path/MANIFEST_NAME).read_text())
 if kind=='checksum':manifest['parts'][0]['sha256']='0'*64
 elif kind=='traversal':manifest['parts'][0]['name']='../financial.parquet'
 elif kind=='duplicate':manifest['parts'][1]['name']=manifest['parts'][0]['name']
 elif kind=='symlink':
  part=path/manifest['parts'][0]['name'];part.unlink();part.symlink_to(public/manifest['parts'][0]['name'])
 elif kind=='canonical_checksum':manifest['canonical_sha256']='0'*64
 elif kind=='unlisted':(path/'unknown.txt').write_text('unlisted')
 elif kind=='rows':manifest['rows']+=1
 elif kind=='schema':manifest['schema'][0][1]='Date'
 (path/MANIFEST_NAME).write_text(json.dumps(manifest))
 before={p.name:(p.lstat().st_size,file_sha256(p)) for p in path.iterdir() if p.is_file()}
 try:materialize_artifact(path);raise AssertionError('accepted corrupt manifest')
 except ValueError as exc:
  after={p.name:(p.lstat().st_size,file_sha256(p)) for p in path.iterdir() if p.is_file()}
  assert path.is_dir() and before==after
  results['negative_controls'][kind]={'rejected':True,'dataset_unchanged':True,'reason':str(exc)}
assert results['bytes_identical'] and results['row_order_and_values_equal'] and results['float32_bits_equal']
Path('docs/maintenance-2026-10-12/mlft-shards-implementation-control.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({k:v for k,v in results.items() if k!='publication_manifest'},indent=2))
