import json
from pathlib import Path
p = Path(r'c:\Users\ricar\OneDrive\Desktop\TESIS\random_forest_borda30.ipynb')
nb = json.loads(p.read_text(encoding='utf-8'))
for cell in nb['cells']:
    if cell.get('cell_type') != 'code':
        continue
    source = ''.join(cell.get('source', []))
    if '# Entrenamiento y evaluación de TabPFN_3' in source:
        new_lines = [
            "if client_available:\n",
            "    # Si no tienes variable de entorno, puedes pegar tu token aquí temporalmente.\n",
            "    tabpfn_token_override = None  # <- reemplaza None con tu API key si lo prefieres\n",
            "\n",
            "    token = (\n",
            "        tabpfn_token_override\n",
            "        or os.getenv('TABPFN_TOKEN')\n",
            "        or os.getenv('TABPFN_API_TOKEN')\n",
            "        or os.getenv('TABPFN_API_KEY')\n",
            "        or globals().get('TABPFN_TOKEN')\n",
            "        or globals().get('TABPFN_API_TOKEN')\n",
            "        or globals().get('TABPFN_API_KEY')\n",
            "    )\n",
            "    if not token:\n",
            "        for candidate in ['tabpfn_token.txt', '.tabpfn_token']:\n",
            "            candidate_path = os.path.join(workspace_dir, candidate)\n",
            "            if os.path.exists(candidate_path):\n",
            "                with open(candidate_path, 'r', encoding='utf-8') as f:\n",
            "                    token = f.read().strip()\n",
            "                if token:\n",
            "                    print(f'Usando token TabPFN desde archivo local: {candidate}')\n",
            "                    break\n",
            "\n",
            "    if token:\n",
            "        try:\n",
            "            set_access_token(token)\n",
            "            print('TabPFN client: access token establecido correctamente.')\n",
            "        except Exception as e:\n",
            "            print('Error estableciendo TabPFN token:', e)\n",
            "            TabPFNClassifier = None\n",
            "    else:\n",
            "        print('No se encontró un token de TabPFN válido.')\n",
            "        print('Define TABPFN_TOKEN en el entorno, o crea un archivo tabpfn_token.txt con tu API key, o asigna tabpfn_token_override en esta celda antes de ejecutar.')\n",
            "        TabPFNClassifier = None\n",
            "\n"
        ]
        cell['source'] = cell['source'][:17] + new_lines + cell['source'][37:]
        p.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding='utf-8')
        print('Fixed cell')
        break
