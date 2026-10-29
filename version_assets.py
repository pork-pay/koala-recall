from pathlib import Path
import hashlib,re,json
O=Path(__file__).resolve().parent;manifest={}
for f in ['app.js','data.js','style.css','memorize.js']:
 p=O/f;h=hashlib.sha256(p.read_bytes()).hexdigest()[:12];name=f'{p.stem}.{h}{p.suffix}';(O/name).write_bytes(p.read_bytes());manifest[f]=name
for page in ['index.html','memorize.html']:
 html=(O/page).read_text()
 for f,name in manifest.items():
  p=O/f
  html=re.sub(r'((?:src|href)=")'+re.escape(p.stem)+r'(?:\.[a-f0-9]{12})?'+re.escape(p.suffix)+r'(?:\?[^" ]*)?"',lambda m:m[1]+name+'"',html)
 (O/page).write_text(html)
print(json.dumps(manifest))
