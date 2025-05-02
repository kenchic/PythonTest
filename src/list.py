listEmployed = ["German Alvarez", "Desarrollador Web", True, "GALVAREZ" , "2500"]
print (listEmployed)

listReadOnly = ("IVA", 1.19)
print (listReadOnly)

print (f"El empleado del mes es {listEmployed[0]}")
print (f"El valor del impuesto {listReadOnly[0]} : {listReadOnly[1]}%")

listSet = {"German Alvarez", "Desarrollador Web", True, "GALVAREZ" , "2500"}
print (listSet)

dictonary = {
    'nombre' : 'German Alvarez',
    'descripcion' : "Desarrollador Web",
    'activo' : True,
    'usuario': 'GAVLAREZ',
    'salario' : 2500
}
print (f"El salario del empleado {dictonary['nombre']} es {dictonary['salario']} USD")

# 1. Crear lista vacía
compras = list()
print("Lista creada:", compras)

# 2. Agregar elementos con append
compras.append("Pan")
compras.append("Leche")
print("\nDespués de append:", compras)

# 3. Insertar elemento en una posición específica
compras.insert(1, "Huevos")
print("\nDespués de insert (posición 1):", compras)

# 4. Agregar varios elementos con extend
compras.extend(["Arroz", "Aceite"])
print("\nDespués de extend:", compras)

# 5. Mostrar la cantidad de elementos con len
print("\nCantidad de elementos:", len(compras))

# 6. Eliminar por índice con pop
eliminado = compras.pop(2)
print("\nDespués de pop (índice 2):", compras)
print("Elemento eliminado:", eliminado)

# 7. Eliminar por valor con remove
compras.remove("Pan")
print("\nDespués de remove ('Pan'):", compras)

# 8. Ordenar la lista (alfabéticamente)
compras.sort()
print("\nDespués de sort:", compras)

# 9. Invertir la lista
compras.reverse()
print("\nDespués de reverse:", compras)

# 10. Eliminar todos los elementos con clear
compras.clear()
print("\nDespués de clear:", compras)
