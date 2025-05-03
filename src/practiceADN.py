

#cadena1 = "ADCCDDDNNDEETSSSS"
#cadena2 = "AAAABBBBDDDDDDRRRADCCD"
# ADCCD

cadena1 = input("Ingresa cadena 1: ")
cadena2 = input("Ingresa cadena 2: ")
indice = 0
cadenaMayorTemp = ''
cadenaMayor = ''

for i in range(len(cadena1))
    for j in range(len(cadena2)):
        if cadena1[i] == cadena2[j]:            



for i in range(len(cadena1)):   
    for j in range(len(cadena2)):
        if cadena1[i] == cadena2[j]:            
            for k in range(i + 1, len(cadena1)):                
                cadenaMayorTemp += cadena1[k]
                if cadena2.find(cadenaMayorTemp)
                                
        else:
            if (len(cadenaMayorTemp) > len(cadenaMayor)):
                cadenaMayor = cadenaMayorTemp
                cadenaMayorTemp = ''
                j = len(cadena2) + 1
            
print(f"Cadena Mayor:{cadenaMayor}")