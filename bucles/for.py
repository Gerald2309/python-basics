animales = ["Perro", "Gato", "Conejo", "Cerdo"]

numeros = [30, 12, 52, 25, 64, 78]

for animal in animales:
    print(animal)
    
    
#Iterar Diferentes listas a la vez
for animal, numero in zip(animales, numeros):
    print(f"Lista de animales: {animal}")
    print(f"Lista de números: {numero}")
    
for i in range(15, 20):
    print(i)
    
    
#Forma no correcta de recorrer listas
for i in range(len(animales)):
    print(f"Animal número {i + 1}:  {animales[i]}")
    


print("   ")
#Recorrer lista con índice
for i in enumerate(animales):
    indice = i[0]
    valor = i[1]
    print(f"Animal número {indice}: {valor}")
    print(f"Animal número {i[0]}: {i[1]}")
    
# Iterar cadenas    
for i in "Geraldine":
    print(i)

print(" ")
texto = "Mundo"
# Iterar al revés
for i in texto[::-1]:
    print(i)
    

##range(inicio, fin, salto)
for i in range(10,0,-2):
    print(i)