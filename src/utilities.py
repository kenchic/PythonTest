def consola(mensaje):
    """
    Funcion que permite mostrar un mensaje en consola
    Args:
        mensaje: cadena que se quiere mostrar en consola
    Ruturns:
        N/A
    """
    print(mensaje)
    
def es_palidromo(palabra):
    """
    Funcion que permite verificar si una palabra es palidrome.
    Args:
        palabra: cadena de entrada para verificar
    Ruturns:
        Si la palabra ingresa es palidrome retorna True de lo contrario False 
    """
    invertido = palabra[::-1]
    resultado = palabra == invertido
    return resultado