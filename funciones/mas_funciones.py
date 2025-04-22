

def frase(nombre, apellido, adjetivo = "gracioso"):
    print(f"{nombre} {apellido} eres muy {adjetivo}")
    
    
frase_nueva = frase(adjetivo="guapo", nombre="Dani", apellido="Naranjo")
print(frase_nueva)