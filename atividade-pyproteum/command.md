
Criar seção
```python3
python3 -m pyproteum testnew --D . --S placar.py placar_session
```

Adicionar arquivos de teste
```python3
python3 -m pyproteum tcase --add --S funcional.py mcdc.py placar_session
```

Gerar mutantes
```
python3 -m pyproteum mutagen --create --all 100 0 placar_session
```

Abre uma UI simples com os mutantes
```python3
python3 -m pyproteum mutaview --gui placar_session
```

Lista os mutantes
```python3
python3 -m pyproteum mutaview --list placar_session
```

Executa os casos de teste em cima dos mutantes
```
python3 -m pyproteum exemuta --exec placar_session
```