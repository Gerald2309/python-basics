

frutas = ["banano", "pera", "manzana", "mora", "mango"]

for fruta in frutas:
    
    if fruta == "pera":
        continue;
    
    print(fruta)
    
print(" ")

for fruta in frutas:
    if fruta == "mora":
        break;
    
    print(fruta)
    
    
    
numeros_duplicados = list()
numeros = [1, 4, 5, 2, 5]
# For en una sola línea

for numero in numeros:
    numeros_duplicados.append(numero * 3)

print(numeros_duplicados)

