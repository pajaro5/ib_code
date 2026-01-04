import random

bingo = []
keep_playing = True

for number in range(1,5): # Crear un array con numeros
    bingo.append(number)

print("Lista original:")
print(bingo)

# Mezclar
random.shuffle(bingo) #Mezclamos la lista
#print("Lista mezclada:")
#print(bingo)

#Jugar
while keep_playing and len(bingo) > 0:
    played_number = random.choice(bingo)
    bingo.remove(played_number)
    print("Número jugado: " + str(played_number))
    
    keep = int(input("Keep playing? 1 Yes / 2 End game: "))

    if keep == 1:
        keep_playing = True
    else:
        keep_playing = False

print("Fin del juego")
