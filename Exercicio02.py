#Declarar
valores: int = [0] * 100
contador: int = 0
media: float = 0.0
maior: int = 0
menor: int = 0
i: int = 0
#Inicio
valores [i] = int(input("Escreva um número:"))
media = valores[i]
menor = valores[i]
maior = valores[i]
contador += 1
for i in range (99):
    valores [i] = int(input("Escreva um número:"))
    if (valores[i]<menor):
        menor = valores[i]
    if (valores[i]>maior):
        maior = valores[i]
    media = valores[i] + media
    contador += 1
media = media / contador
print("Essa é a média dos números digitados:",media)
print ("Esse é o maior número:",maior)
print ("Esse é o menor número:",menor)
#Fim