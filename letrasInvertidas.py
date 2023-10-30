def inverter_letras_palavras(frase):
    # Divide a frase em palavras
    palavras = frase.split()

    # armazena as palavras invertidas
    palavras_invertidas = []

    # Inverte as letras de cada palavra e adiciona à lista
    for palavra in palavras:
        palavra_invertida = palavra[::-1]
        palavras_invertidas.append(palavra_invertida)

    # Junta as palavras invertidas em uma nova frase
    nova_frase = ' '.join(palavras_invertidas)

    return nova_frase

# Exemplo de uso da função
frase = "Aproveite o dia"
frase_invertida = inverter_letras_palavras(frase)
print(f"Frase original: {frase}")
print(f"Frase com palavras invertidas: {frase_invertida}")
