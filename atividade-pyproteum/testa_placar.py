import os

# Limpeza rápida para garantir que não dê erro de "sessão já existe" ao rodar de novo
# if os.path.exists("placar_session.xsml"):
#     os.remove("placar_session.xsml")
# if os.path.exists("placar_session.db"):
#     os.remove("placar_session.db")

os.system("python3 -m pyproteum testnew --D . --S placar.py placar_session")

# Adiciona funcional.py e mcdc.py na mesma linha conforme seu comando
os.system("python3 -m pyproteum tcase --add --S funcional.py mcdc.py placar_session")

os.system("python3 -m pyproteum mutagen --create --all 100 0 placar_session")

os.system("python3 -m pyproteum exemuta --exec placar_session")

os.system("python3 -m pyproteum exemuta --equiv --x 648 placar_session")