lista = ["Hola,", "Segundo elemento", 3 ]
lista[2] = "Tercer elemento";

print(lista)

tupla = ("Esto es una tupla", "No se puede modificar")

print(tupla)

conjunto = {"esto es un conjunto", "o", "un set", "los elementos no se pueden modificar"}
print(conjunto)
conjunto = {"Pero se pueden", "redefinir"}
print(conjunto)

diccionario = {
    "nombre" : "Geraldine",
    "email" : "geral@gmail.com",
    "altura" : 1.60
}
print(diccionario["nombre"])

diccionario["nombre"] = "Daniel"
print(diccionario["nombre"])


#### Ejercicio

frutas = ["banano", "pera", "mango"]

frutas.append("mora") 

print(frutas)