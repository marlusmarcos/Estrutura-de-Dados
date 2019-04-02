

ss = 'eduadrowqnsr'
lista_apoio = set ()
cont=0;
maior = 0;
for i in ss:
    if i not in lista_apoio:
        lista_apoio.add(i)
        cont = cont+1
    else:
        if cont > maior:
            maior = cont;
print (maior)