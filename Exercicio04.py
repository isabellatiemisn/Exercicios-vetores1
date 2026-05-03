#Declarar
notas: float = [0.0] * 30
media: float = 0.0
abaixo: int = [0] * 30
acima: int = 0
#Inicio
for i in range (30): 
    notas[i] = float(input("Coloque a nota:"))
    media =  notas[i] + media
media = media / 30
i = 0
for i in range (30):
    if (media<notas[i]):
        acima += 1 
i = 0
n = 0
for i in range (30):
    if (media>notas[i]):
        abaixo[n] = i
        n += 1
print ("Essa é a média das notas:",media)
print("Essa é a quantidade de notas acima da média:",acima)
print ("Essas são as posições das notas abaixo da média:",abaixo[:n])
#Fim