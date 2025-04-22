
num1 = 8
num2 = 7


def saludar():
    print("Este es un saludo")
    
    
def sumar(num1, num2):
    print(num1 + num2)
    
    
    
    
saludar() 
sumar(num1, num2)
sumar(3,8)

# Función que retorna
def crear_contraseña_random(num):
    listado_de_caracteres = "adfnjrnuds"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num -2
    c2 = num
    c3 = num -5
    contraseña = f"{listado_de_caracteres[c1]}{listado_de_caracteres[c3]}{num * 2 }"
    return contraseña
    
    
password = crear_contraseña_random(3)
print(password)