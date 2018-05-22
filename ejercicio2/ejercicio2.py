
'''
IMF Big Data Master ejercicio 2 modulo 1
Juan Iglesias Cavada

Este programa lee tweets del archivo tweets.txt y encuentra las palabras que no tienen equivalencia en
el diccionario sentimientos.txt. Posteriormente les asigna el valor del sentimiento del tweet en el que
se encuentran y las muestra.

'''
def get_sentimientos(archivo):
    '''
    lee el archivo de términos y devuelve un diccionario creado con los mismos
    '''
    with open(archivo, 'r') as sentimientos:
        valores = {}
        for linea in sentimientos:
            termino,valor = linea.split('\t')
            valores[termino] = int(valor)
    return valores


valores = get_sentimientos("Sentimientos.txt")
with open('tweets.txt', 'r') as tweets:
    for tweet in tweets:
        if len(tweet) < 2: #excluye tweets que tengan menos de 2 caracteres, siendo uno \n
            continue
        print('\n' + tweet)
        words_not_rated = []
        sentiment = 0
        for word in tweet.split(): #para cada palabra ver si existe en el diccionario y actualiza su sentimiento
            if word in valores:
                sentiment += valores[word]
            else:
                words_not_rated.append(word)
        for word in words_not_rated:
            print(word + ':' + str(sentiment))

        

