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

if dictonary['usuario'] == "GALVAREZ":
    if dictonary['clave'] == "1234":
        print("Acceso concedido")
        
        bonoTareasFinalizadas1 = 10
        bonoTareasFinalizadas2 = 8

        if dictonary['tareasFinalizadas'] > bonoTareasFinalizadas1:
            print(f"{dictonary['nombre']} tiene bono 100%")
        elif dictonary['tareasFinalizadas'] > bonoTareasFinalizadas2:
            print(f"{dictonary['nombre']} tiene bono 80%")
        else:
            print(f"{dictonary['nombre']} no cumplio para el bono")  
            
        es_admin = False
        es_supervisor = True

        if dictonary['rol'] == 'admin' or dictonary['clave'] == 'supervisor':
            print("Puede ejecutar la acción")  
        else:
            print("No puede ejecutar la acción")

        
    else:
        print("Usuario/Contraseña incorrecta")
else:
    print("Usuario no reconocido")
