listEmployed = ["German Alvarez", "Desarrollador Web", True, "GALVAREZ" , "1000"]
print (listEmployed)

listReadOnly = ("IVA", 1.19)
print (listReadOnly)

print (f"El empleado del mes es {listEmployed[0]}")
print (f"El valor del impuesto {listReadOnly[0]} : {listReadOnly[1]}%")

listSet = {"German Alvarez", "Desarrollador Web", True, "GALVAREZ" , "1000"}
print (listSet)

dictonary = {
    'nombre' : 'German Alvarez',
    'descripcion' : "Desarrollador Web",
    'activo' : True,
    'usuario': 'GAVLAREZ',
    'salario' : 1000
}
print (f"El salario del empleado {dictonary['nombre']} es {dictonary['salario']} USD")
