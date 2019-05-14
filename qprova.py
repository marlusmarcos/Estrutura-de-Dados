class Solution:
def divisorGame(self, N: int) -> bool:
cont = 1 #contador que inicializei impar que significa que está na rodada da garota
x = N-1
if N == 2:
return True
while x > 1:
if N%x == 0:
cont = cont +1
N = N-x
x = N-1
x = x-1
if cont%2 == 0:
return True
return False
