#Se crea una lista de los valores de moneda disponible y una lista 
#del mismo tamaño que guardada la cantidad utilizada de cada moneda
monedas_disp = [1, 5, 10, 20, 50, 100]
monedas_usadas = [0] * len(monedas_disp)
mascara = [0] * len(monedas_disp)

#Se declara el valor de la moneda a cambiar 
quiero_cambiar = 25
falta_por_pagar = quiero_cambiar
#Guarda la acumulacion que permitira encontrar otros casos 
acumulacion = 0

#Declaramos un entero que disminuira el valor de las monedas utilizadas
regresion = len(monedas_disp) - 1

#Guarda los casos
caso = 0

#Bucamos el caso maximo para saber con que denominacion de moneda se va a iniciar
while 1 :
    if quiero_cambiar >= monedas_disp[regresion]:
        if regresion > 0:
            ciclos = regresion
            subciclos = ciclos -1
        else:
            ciclos = regresion
            subciclos = ciclos
        break
    else:
        regresion -= 1
        
mascara[ciclos] = 1    

#Ciclo que busca todos los casos disponibles
while 1 :
    # Conjunto de resta la denominacion correpondiente de lo que falta por pagar
    if falta_por_pagar >= monedas_disp[regresion]:
        falta_por_pagar -= monedas_disp[regresion]
        monedas_usadas[regresion] += 1 
    else:
        regresion -= 1
    # si lo que falta por pagar es igual a 0 entonces:    
    if falta_por_pagar == 0:
        
        #Se imprime el caso correspondiente 
        caso +=1
        print(f"Caso {caso} - monedas usadas de: 1 : {monedas_usadas[0]} | 5 : {monedas_usadas[1]} | 10 : {monedas_usadas[2]} | 20 : {monedas_usadas[3]} | 50 : {monedas_usadas[4]} | 100 : {monedas_usadas[5]}")
        
        #Se buscan todas las combinaciones por debajo del valor maximo de denominacion
        while 1:
            if monedas_usadas[subciclos] > 0 and subciclos != 0: 
                mascara[subciclos] = 1 
                regresion = subciclos - 1
                monedas_usadas[subciclos] -= 1
                for i in range(len(monedas_disp) - 1):
                    monedas_usadas[i] *= mascara[i]
                
                for i in range(len(monedas_disp)):
                    acumulacion += monedas_usadas[i] * monedas_disp[i]
                
                falta_por_pagar = quiero_cambiar - acumulacion
                acumulacion = 0
                break
            else:
                subciclos -= 1  
                if subciclos == 0:
                    break

    #si ya no quedan mas combinaciones por debajo de la denominacion maxima utilizada 
    #se empezara a reducir la cantidad de monedas de mayor denomicacion utilizadas 
    #hasta que estas sean 0
    if subciclos == 0 and falta_por_pagar == 0:
        mascara = [0] * len(monedas_disp)
        mascara[ciclos] = 1 
        while 1:
            if monedas_usadas[ciclos] > 0:
                #mascara[subciclos] = 1 
                regresion = ciclos - 1
                subciclos = ciclos -1
                monedas_usadas[ciclos] -= 1
                for i in range(len(monedas_disp) - 1):
                    monedas_usadas[i] *= mascara[i]
                
                for i in range(len(monedas_disp)):
                    acumulacion += monedas_usadas[i] * monedas_disp[i]
                
                falta_por_pagar = quiero_cambiar - acumulacion
                acumulacion = 0
                break
            else:
                ciclos -= 1 
                
                
    if regresion < 0:
        break
    # se establece una condicion para romper el ciclo y terminar
    if ciclos == 0:    
       break
