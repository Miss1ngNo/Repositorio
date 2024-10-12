# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 23:03:56 2024

@author: angel
"""

#Se crea una lista de los valores de moneda disponible y una lista 
#del mismo tamaño que guardada la cantidad utilizada de cada moneda
monedas_disp = [1, 5, 10, 20, 50, 100]
monedas_usadas = [0] * len(monedas_disp)
mascara = [0] * len(monedas_disp)

#Se declara el valor de la moneda a cambiar 
quiero_cambiar = 100
falta_por_pagar = quiero_cambiar

#Declaramos un entero que disminuira el valor de las monedas utilizadas
regresion = len(monedas_disp) - 1

caso = 0

while 1 :
    if quiero_cambiar >= monedas_disp[regresion]:
        valor_max = monedas_disp[regresion]
        ciclos = regresion
        subciclos = ciclos -1
        break
    else:
        regresion -= 1
        
while ciclos >= 0 :
    if falta_por_pagar >= monedas_disp[regresion]:
        falta_por_pagar -= monedas_disp[regresion]
        monedas_usadas[regresion] += 1 
    else:
        regresion -= 1
    if falta_por_pagar == 0:
        caso +=1
        
        #print(f"Caso {caso} - monedas usadas de: 1 : {monedas_usadas[0]} | 5 : {monedas_usadas[1]} | 10 : {monedas_usadas[2]} | 20 : {monedas_usadas[3]} | 50 : {monedas_usadas[4]} | 100 : {monedas_usadas[5]}")    
        print(f"{caso}  {monedas_usadas[0]} {monedas_usadas[1]} {monedas_usadas[2]} {monedas_usadas[3]} {monedas_usadas[4]} {monedas_usadas[5]}" )
        
        for i in range(subciclos, -1, -1):
            if monedas_usadas[i] > 0 and subciclos >= 0 :
                subciclos = i
                monedas_usadas[i] -= 1 
                if monedas_usadas[i] > 0:
                    for x in range(0, subciclos, 1):
                        monedas_usadas[x] = monedas_usadas[x] * 0
                    for x in range(ciclos, 0, -1):
                        falta_por_pagar += monedas_usadas[x]*monedas_disp[x]
                    falta_por_pagar = quiero_cambiar - falta_por_pagar
                    regresion = i - 1
                else:  
                    for x in range(subciclos, -1, -1):
                        monedas_usadas[x] = monedas_usadas[x] * 0
                    subciclos -= 1
                    for x in range(ciclos, 0, -1):
                        falta_por_pagar += monedas_usadas[x]*monedas_disp[x]
                    falta_por_pagar = quiero_cambiar - falta_por_pagar
                    regresion = subciclos
          
        if subciclos == 0 and falta_por_pagar == 0:
            monedas_usadas[ciclos] -= 1
            if monedas_usadas[ciclos] > 0:
                mascara[ciclos] = 1
                monedas_usadas = monedas_usadas and mascara
                for x in range(ciclos, 0, -1):
                    falta_por_pagar += monedas_usadas[x]*monedas_disp[x]
                falta_por_pagar = quiero_cambiar - falta_por_pagar
                regresion = ciclos - 1
                subciclos = ciclos - 1
            else:
                ciclos -= 1
                regresion = ciclos
                subciclos = ciclos - 1
                falta_por_pagar = quiero_cambiar
                monedas_usadas = [0] * len(monedas_disp)    
                  
    if falta_por_pagar == 0 and ciclos == 0 and subciclos == 0:    
        break
