from datetime import datetime

# Solicita o nome.
nome = input("Digite o nome da pessoa: ")

# Solicita o ano de nascimento.
ano_nascimento = int(input(f"Digite o ano de nascimento: "))
mes_nascimento = int(input(f"Digite o mês de nascimento: "))
dia_nascimento = int(input(f"Digite o dia de nascimento: "))

# Cria data de nascimento com base nas entradas.
data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)

# Define data atual como 2023-01-01
data_atual = datetime(2023, 10, 30)

# Calcula a diferença entre a data atual (2023-10-30) e a data de nascimento
diferenca = data_atual - data_nascimento

# Extrai anos, meses e dias da diferença
anos = diferenca.days // 365
meses = (diferenca.days % 365) // 30
dias = (diferenca.days % 365) % 30

#resultado
print(f"{nome} tem {anos} anos, {meses} meses e {dias} dias de idade.")



