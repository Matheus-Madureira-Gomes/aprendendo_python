from pathlib import Path

caminho = Path()
print(caminho.absolute())

arquivo = Path.home() / 'arquivoExemplo.txt'

arquivo.touch()
print(arquivo)
arquivo.write_text('Olá mundo!')
print(arquivo.read_text())
arquivo.unlink()