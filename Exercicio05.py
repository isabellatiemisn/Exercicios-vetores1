#Declarar
vetor1: int = [0] * 20
vetor2: int = [0] * 10
soma: int = 0
#Inicio
for i in range (20):
    vetor1[i]= int(input("Digite um número:"))
i = 0
l=0
for i in range (10):
    vetor2[l] = vetor1 [i] - vetor1[19-i]
    l += 1
l=0
while (l<10):
    soma = vetor2[l]+soma
    l+=1
print (soma)
#Fim