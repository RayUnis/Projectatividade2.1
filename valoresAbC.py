# Solicita três valores a, b e c
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

# Verifica se os valores formam um triângulo
if a < b + c and b < a + c and c < a + b:
    # Calcula o semiperímetro
    s = (a + b + c) / 2
    # Calcula a área usando a fórmula de Heron
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f"Os valores {a}, {b} e {c} formam um triângulo com área de {area:.2f}.")
else:
    print(f"Os valores {a}, {b} e {c} não formam um triângulo.")
