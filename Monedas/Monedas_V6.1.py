#Se crea una lista de los valores de moneda disponible y una lista 
#del mismo tamaño que guardada la cantidad utilizada de cada moneda
monedas_disp = [1, 5, 10, 20, 50, 100]
monedas_usadas = [0] * len(monedas_disp)
mascara = [0] * len(monedas_disp)

#Se declara el valor de la moneda a cambiar 
quiero_cambiar = 120
falta_por_pagar = quiero_cambiar
acumulacion = 0

#Declaramos un entero que disminuira el valor de las monedas utilizadas
regresion = len(monedas_disp) - 1

caso = 0

no_hay_subciclos = False
no_hay_ciclos = False

while 1 :
    if quiero_cambiar >= monedas_disp[regresion]:
        if regresion > 0:
            ciclos = regresion
            subciclos = ciclos -1
        else:
            ciclos = regresion
            subciclos = ciclos
            no_hay_subciclos = True
        break
    else:
        regresion -= 1
        
ptr = subciclos    
mascara[ciclos] = 1    
while ciclos >= 0 :
    if regresion < 0:    
        break
    if falta_por_pagar >= monedas_disp[regresion]:
        falta_por_pagar -= monedas_disp[regresion]
        monedas_usadas[regresion] += 1 
    else:
        regresion -= 1
    if falta_por_pagar == 0:
        caso +=1
        
        #print(f"Caso {caso} - monedas usadas de: 1 : {monedas_usadas[0]} | 5 : {monedas_usadas[1]} | 10 : {monedas_usadas[2]} | 20 : {monedas_usadas[3]} | 50 : {monedas_usadas[4]} | 100 : {monedas_usadas[5]}")    
        print(f"{caso}  {monedas_usadas[0]} {monedas_usadas[1]} {monedas_usadas[2]} {monedas_usadas[3]} {monedas_usadas[4]} {monedas_usadas[5]}" )
        
        while subciclos > 0:
            if monedas_usadas[ptr] > 0:
                mascara[ptr] = 1 
                #subciclos -= 1
                regresion = ptr - 1
                monedas_usadas[ptr] -= 1
                for i in range(len(monedas_disp) - 1):
                    monedas_usadas[i] *= mascara[i]
                
                for i in range(len(monedas_disp) - 1):
                    acumulacion += monedas_usadas[i] * monedas_disp[i]
                
                falta_por_pagar = quiero_cambiar - acumulacion
                acumulacion = 0
                break
            else:
                ptr -= 1  
            #    if 10 == ptr:
            #        no_hay_subciclos = True   
    
    #if regresion < 0:    
    #   break
