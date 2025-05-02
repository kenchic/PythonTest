bonoTareasFinalizadas1 = 10
bonoTareasFinalizadas2 = 8

dictonary = {
    'nombre' : 'German Alvarez',
    'descripcion' : "Desarrollador Web",
    'activo' : True,
    'usuario': 'GAVLAREZ',
    'salario' : 2500,
    'tareasFinalizadas': 9
}

if dictonary['tareasFinalizadas'] > bonoTareasFinalizadas1:
    print(f"{dictonary['nombre']} tiene bono 100%")
elif dictonary['tareasFinalizadas'] > bonoTareasFinalizadas2:
    print(f"{dictonary['nombre']} tiene bono 80%")
else:
    print(f"{dictonary['nombre']} no cumplio para el bono")    
    