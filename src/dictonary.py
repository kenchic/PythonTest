dictonary = {
    'nombre' : 'German Alvarez',
    'descripcion' : "Desarrollador Web",
    'activo' : True,
    'usuario': 'GALVAREZ',
    'rol' : 'ventas',
    'clave' : "1234",
    'salario' : 2500,
    'tareasFinalizadas': 9
}


# 1. Crear diccionario de contactos
contactos = {
    "Juan": "3011234567",
    "Ana": "3029876543",
    "Luis": "3001112233"
}
print("Diccionario original:", contactos)

# 2. Mostrar todas las claves (nombres)
print("\nClaves (nombres de contactos):")
print(contactos.keys())

# 3. Obtener el número de un contacto con get()
print("\nNúmero de Ana:", contactos.get("Ana"))

# 3. Obtener manualmente número de Luis
for nombre, telefono in contactos.items():
    if nombre == 'Luis' :
        print ( f" telefono de luis es:{telefono}")

# 4. Eliminar un contacto con pop()
eliminado = contactos.pop("Luis")
print("\nSe eliminó a Luis con número:", eliminado)
print("Diccionario actual:", contactos)

# 5. Iterar con items()
print("\nLista de contactos:")
for nombre, telefono in contactos.items():
    print(f"{nombre}: {telefono}")



# 6. Eliminar todos los contactos
contactos.clear()
print("\nDiccionario después de clear():", contactos)
