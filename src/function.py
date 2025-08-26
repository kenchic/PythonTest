def mostrar_datos_cuenta(**kwargs):
    print("📋 Detalles de la cuenta:")
    for clave, valor in kwargs.items():
        print(f"🔹 {clave.capitalize()}: {valor}")

        
numeros = [1 , 5, 3, 9, 12, 5]
numero_maximo = max(numeros)
numero_minimo = min(numeros)
print (f"numero mas alto: {numero_maximo}")
print (f"numero mas bajo: {numero_minimo}")

mostrar_datos_cuenta(
    nombre="Luis García",
    tipo_cuenta="Ahorros",
    saldo=15000
)

def es_palidromo(palabra):
    invertido = palabra[::-1]
    resultado = palabra == invertido
    return resultado

palabra = input("Ingrese palabra: ")

if es_palidromo(palabra):
    print (f"la palabra {palabra} es correcta")
else: 
    print (f"la palabra {palabra} no es correcta")
    
    
def funcion_documentada(mensaje):
    """
    Muestra un mensaje en la pantalla
    
    Args:
        mensaje(string): mensaje para mostrar en pantalla
    
    Returns:
        N/A
    """
    print (mensaje)

funcion_documentada('mostrar este mensaje')

def dividir(cociente, divisor):
    """
    Funcion que divide un numero por otro
    Args:
        cociente: número cociente a ser dividido
        divisor: número en el que se divide
    Ruturns:
        Devuelve el valor de la división
    """
    try:
        resultado = cociente / divisor
        return resultado
    except ZeroDivisionError:
        return 0
    
print (dividir(2,4))
print (dividir(9,0))
