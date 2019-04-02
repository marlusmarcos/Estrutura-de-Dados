from random import randint
primos = set()


while len(primos) < 5:
  cont=0
  num = (randint(2,100))
  for a in range (1,num+1):
    if num%a == 0:
      cont=cont+1
  if cont == 2:
    primos.add(num)
    
print ("Conjunto a =", primos)