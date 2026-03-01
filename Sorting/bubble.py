#Bubble sort demo

samples = [8,4,2,6,1]

print("Lista original: ")
print(samples)
number_of_elements = len(samples)

for i in range(len(samples)):
    for j in range(0, number_of_elements-i-1 ):
        #comparamos el elemento actual con el siguiente
        if samples[j] > samples[j+1]:
            #si están en orden incorrecto, los intercambiamos
            samples[j], samples[j+1] = samples[j+1], samples[j]


print("lista ordenada")
print(samples)