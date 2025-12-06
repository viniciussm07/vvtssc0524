import os
import subprocess

# Configurações
PYTHON = "python3" # Ou "python" no Windows
SESSION = "placar_session"
OUTPUT_FILE = "relatorio_vivos.txt"

# 1. Obter a lista de todos os mutantes vivos
print("Obtendo lista de mutantes vivos...")
cmd_list = f"{PYTHON} -m pyproteum mutaview --list {SESSION}"
result = subprocess.run(cmd_list, shell=True, capture_output=True, text=True)
lines = result.stdout.splitlines()

# Filtra apenas os IDs que estão "live"
live_ids = []
for line in lines:
    parts = line.split()
    # O formato geralmente é: ID  OPERADOR  STATUS
    # Ex: 0079  cccr  live
    if len(parts) >= 3 and parts[2] == "live":
        live_ids.append(parts[0])

print(f"Encontrados {len(live_ids)} mutantes vivos.")

# 2. Para cada vivo, pegar o código fonte e salvar no arquivo
print(f"Gerando relatório em {OUTPUT_FILE}...")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for mid in live_ids:
        print(f"Processando mutante {mid}...")
        
        f.write(f"{'='*40}\n")
        f.write(f"MUTANTE ID: {mid}\n")
        f.write(f"{'='*40}\n")
        
        cmd_view = f"{PYTHON} -m pyproteum mutaview --view --x {mid} {SESSION}"
        res_view = subprocess.run(cmd_view, shell=True, capture_output=True, text=True)
        
        f.write(res_view.stdout)
        f.write("\n\n")

print("Concluído! Abra o arquivo 'relatorio_vivos.txt' para ver os códigos.")