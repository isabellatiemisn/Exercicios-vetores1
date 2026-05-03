#Declarar
vetor: float = [0.0] * 5
temp: float = 0.0
valor: float = 0.0
inicio: int = 0
fim: int = 0
#inicio
for i in range (5):
    vetor[i] =  float(input("Digite um número:"))
for i in range(5):
    for l in range(5):
        if vetor[i] < vetor[l]:
            temp = vetor[i]
            vetor[i] = vetor[l]
            vetor[l] = temp
valor = float(input("Coloque um valor:"))
fim = (len(vetor)-1)
while (inicio<=fim):
    meio = (inicio+fim)//2
    if (valor==vetor[meio]):
        print ("O número:", valor, "tem no vetor")
        break
    elif (valor>vetor[meio]):
        inicio = meio + 1
    else:
        fim = meio - 1
else:
    print ("O número:", valor, "não tem no vetor")

#Fim