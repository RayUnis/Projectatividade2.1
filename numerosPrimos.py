# verificar se um número é primo
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

# Testa a função de 1 a 100
for num in range(1, 100):
    if is_prime(num):
        print(f"{num} é primo.")
