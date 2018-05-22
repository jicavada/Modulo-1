

with open("Sentimientos.txt", 'r') as sentimientos:
    valores = {}
    for linea in sentimientos:
        termino,valor = linea.split('\t')
        valores[termino] = int(valor)

print(valores['collapse'])