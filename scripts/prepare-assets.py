from pathlib import Path
import hashlib, re
root = Path(__file__).resolve().parent.parent / 'dist'
html = (root / 'index.html').read_text()
for filename in ['game.js', 'style.css']:
    source = root / filename
    digest = hashlib.sha256(source.read_bytes()).hexdigest()[:10]
    target = source.stem + '.' + digest + source.suffix
    (root / target).write_bytes(source.read_bytes())
    html = re.sub(r'"' + re.escape(source.stem) + r'(?:\.[0-9a-f]{10})?' + re.escape(source.suffix) + r'"', '"' + target + '"', html)
(root / 'index.html').write_text(html)
print('Asset references synchronized')
