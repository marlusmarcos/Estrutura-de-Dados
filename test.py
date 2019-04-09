lista = ["marcos","mateus","marlus"]
lista_saida = []
tam_entrada = len(lista)

primeiro_nome = lista[0]
'''menor = len(primeiro_nome)

for h in range (0,tam_entrada):
	if menor > len(lista[h]):
		primeiro_nome = lista[h]
		menor = len(lista[h])'''

tam_first_name = len (primeiro_nome)

for i in range (0,tam_first_name):
	cont = 0
	vogal = primeiro_nome[i]
	for j in range (0,tam_entrada):
		if vogal in lista[j]:
			cont = cont +1
	if cont == tam_entrada:
		lista_saida.append(vogal)
		
print (lista_saida)