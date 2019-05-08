
lista_retorno = set()
controle = 1
numrs = [2,7,11,15]
alvo=9
i=0
j=len(numrs)-1

while controle == 1:
	if numrs[i] + numrs[j] == alvo:
		lista_retorno.add(i)
		lista_retorno.add(j)
		controle = 0
	if numrs[i] + numrs[j] > alvo:
		j = j-1
	if numrs[i] + numrs[j] < alvo:
		i = i+1
#return lista_retorno
numrs = [2,7,11,15]
alvo=9
print (lista_retorno)

##############
#meu nome é Marlus Marcos
