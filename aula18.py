# Exemplo de variável global
contador = 10

def minha_funcao():
  # Para modificar a variável global, use 'global'
  global contador
  contador = contador + 5
  print(f"Dentro da função: {contador}")

print(f"Antes da função: {contador}")
minha_funcao()
print(f"Depois da função: {contador}")
