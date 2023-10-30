# Solicita os três números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

# Inicio variável
menor = numero1

# Verifica se o segundo número é menor que o primeiro
if numero2 < menor:
    menor = numero2

# Verifica se o terceiro número é menor que o atual 'menor'
if numero3 < menor:
    menor = numero3

# Exibe o menor número
print(f"O menor número é: {menor}")
