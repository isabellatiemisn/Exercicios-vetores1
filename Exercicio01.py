#Declarar
valores: int = [0] * 50  
impares: int = 0
media: float = 0
contador: int = 0
#Inicio
for i in range (50):
    valores [i] = int(input("Escreva um número:"))
    if (10<valores[i]<200):
        contador += 1
        print (contador)
        media = media + valores[i]
    if (valores[i]%2==1):
        impares = impares + valores[i]
if (contador>0):
    media = media / contador
print ("Essa é a média dos valores entre 10 e 200:",media)
print ("Essa é a soma dos ímpares:",impares)
#Fim