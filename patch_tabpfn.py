import json
from pathlib import Path
p = Path(r'c:\Users\ricar\OneDrive\Desktop\TESIS\random_forest_borda30.ipynb')
nb = json.loads(p.read_text(encoding='utf-8'))
for cell in nb['cells']:
    if cell.get('cell_type') != 'code':
        continue
    source = ''.join(cell.get('source', []))
    if '# Entrenamiento y evaluación de TabPFN_3' in source:
        old = ''.join(cell['source'][17:26])
        new = (
            'if client_available:\n'
            '    # Si no tienes variable de entorno, puedes pegar tu token aquí temporalmente.\n'
            '    tabpfn_token_override = None  # <- reemplaza None con tu API key si lo prefieres\n'
            '\n'
            '    token = (\n'
            '        tabpfn_token_override\n'
            '        or os.getenv(\'TABPFN_TOKEN\')\n'
            '        or os.getenv(\'TABPFN_API_TOKEN\')\n'
            '        or os.getenv(\'TABPFN_API_KEY\')\n'
            '        or globals().get(\'TABPFN_TOKEN\')\n'
            '        or globals().get(\'TABPFN_API_TOKEN\')\n'
            '        or globals().get(\'TABPFN_API_KEY\')\n'
            '    )\n'
            '    if not token:\n'
        )
        if old not in source:
            raise SystemExit('Exact block not found to replace')
        source = source.replace(old, new, 1)
        cell['source'] = source.splitlines(keepends=True)
        p.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding='utf-8')
        print('Patched cell')
        break
