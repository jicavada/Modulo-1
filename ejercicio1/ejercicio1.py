
'''
IMF Big Data Master ejercicio 1 modulo 1
Juan Iglesias Cavada

El programa lee tweets de un archivo tweets.txt y muestra el valor del sentimiento asociado.
Los valores de sentimiento se calculan en base a un diccionario dado en sentimientos.txt que asocia ciertos
términos a un valor numérico que describe su sentimiento.
Si el tweet contiene uno o varios términos existentes en el diccionario, se calcula su sentimiento.
Finalmente muestra el tweet y el sentimiento asociado al mismo
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
        
        sentiment = 0
        for word in tweet.split(): #para cada palabra ver si existe en el diccionario y actualiza su sentimiento
            if word in valores:
                sentiment += valores[word]
        print('tweet: ' + tweet + "El valor del sentimiento es:" + str(sentiment) + '\n')

