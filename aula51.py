from pathlib import Path

caminho = Path('C:/Users/mathe/images')

for pasta in caminho.iterdir():
    if pasta.is_dir():
        print(pasta.name)
        for imagem in pasta.iterdir():
            print('  ', imagem)