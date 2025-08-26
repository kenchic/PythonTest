with open("datos.txt", "w") as archivo:
    archivo.write("Primera línea.\n")
    archivo.write("Segunda línea.\n")
    
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
    
with open("datos.txt", "a") as archivo:
    archivo.write("Tercera línea.\n")
    
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)