#Declarar
vetor: float = [0.0] * 5
temp: float = 0.0
#inicio
for i in range (5):
    vetor[i] =  float(input("Digite um número:"))
for i in range(5):
    for l in range(5):
        if vetor[i] < vetor[l]:
            temp = vetor[i]
            vetor[i] = vetor[l]
            vetor[l] = temp
print (vetor)
#Fim