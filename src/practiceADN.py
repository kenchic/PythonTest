

#cadena1 = "ADCCDDDNNDEETSSSS"
#cadena2 = "AAAABBBBDDDDDDRRRADCCD"
# ADCCD

cadena1 = input("Ingresa cadena 1: ").upper()
cadena2 = input("Ingresa cadena 2: ").upper()
cadenaMayorTemp = ''
cadenaMayor = ''

for i, c in enumerate(cadena1) :
    if  cadena2.find(c) != -1:
        for j in range(i + 1, len(cadena1) + 1):
            cadenaMayorTemp = cadena1[i:j]   
            if  cadena2.find(cadenaMayorTemp) == -1:
                    cadenaMayorTemp = ''
            elif len(cadenaMayorTemp) > len(cadenaMayor):
                    cadenaMayor = cadenaMayorTemp
            
print(f"Cadena Mayor:{cadenaMayor}")