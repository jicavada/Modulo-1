

with open("Sentimientos.txt", 'r') as sentimientos:
    valores = {}
    for linea in sentimientos:
        termino,valor = linea.split('\t')
        valores[termino] = int(valor)

valores = get_sentimientos("Sentimientos.txt")
with open('tweets.txt', 'r') as tweets:
    for tweet in tweets:
