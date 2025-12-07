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
os.system("python3 -m pyproteum exemuta --equiv --x 0079 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0080 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0159 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0184 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0187 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0217 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0220 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0221 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0230 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0232 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0238 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0239 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0245 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0248 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0249 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0253 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0254 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0255 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0302 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0304 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0306 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0307 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0318 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0327 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0336 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0342 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0530 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0531 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 0532 placar_session")

os.system("python3 -m pyproteum exemuta --equiv --x 1208 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 1179 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 1174 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 1164 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 1159 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 1154 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 1149 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 1144 placar_session")
os.system("python3 -m pyproteum exemuta --equiv --x 1139 placar_session")


os.system("python3 -m pyproteum exemuta --exec placar_session")