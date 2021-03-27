cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):")
if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
if (cadena.count('!') + cadena.count('@') != 0):
    print("Ingresaste alguno de estos símbolos: @ o !" )
else:
    print("Ingreso OK")