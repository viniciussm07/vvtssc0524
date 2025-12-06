# Fabio Alves dos Santos - 15494462
# Gabriel Huemer - 15453470
# Vinicius Soares Martins - 11794907

import os

# Limpeza rápida para garantir que não dê erro de "sessão já existe" ao rodar de novo
# if os.path.exists("placar_session.xsml"):
#     os.remove("placar_session.xsml")
# if os.path.exists("placar_session.db"):
#     os.remove("placar_session.db")

os.system("python3 -m pyproteum testnew --D . --S placar.py placar_session")

os.system("python3 -m pyproteum tcase --add --S funcional.py placar_session")
os.system("python3 -m pyproteum tcase --add --S mcdc.py placar_session")
os.system("python3 -m pyproteum tcase --add --S mutation.py placar_session")

os.system("python3 -m pyproteum mutagen --create --all 100 0 placar_session")

# os.system("python3 -m pyproteum exemuta --equiv --x 648 placar_session")
# os.system("python3 -m pyproteum exemuta --equiv --x 635 placar_session")
# os.system("python3 -m pyproteum exemuta --equiv --x 638 placar_session")

os.system("python3 -m pyproteum exemuta --exec placar_session")