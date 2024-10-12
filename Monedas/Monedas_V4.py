# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 23:03:56 2024

@author: angel
"""

#Se crea una lista de los valores de moneda disponible y una lista 
#del mismo tamaño que guardada la cantidad utilizada de cada moneda
MonedasDisp = [1, 5, 10, 20, 50, 100]
MonedasUsadas = [0] * len(MonedasDisp)
mascara = [0] * len(MonedasDisp)

#Se declara el valor de la moneda a cambiar 
Quiero_cambiar = 25
Falta_por_Pagar = Quiero_cambiar

#Declaramos un entero que disminuira el valor de las monedas utilizadas
Regresion = len(MonedasDisp) - 1
count = Regresion

caso = 0

while 1 :
    if Quiero_cambiar >= MonedasDisp[count]:
        valor_max = MonedasDisp[count]
        break
    else:
        count -= 1
        
while 1:
    if Falta_por_Pagar >= MonedasDisp[Regresion]:
        Falta_por_Pagar -= MonedasDisp[Regresion]
        MonedasUsadas[Regresion] += 1 
    else:
        Regresion -= 1
    if Falta_por_Pagar == 0:
        caso +=1
        print(f"Caso {caso} - monedas usadas de: 1 : {MonedasUsadas[0]} | 5 : {MonedasUsadas[1]} | 10 : {MonedasUsadas[2]} | 20 : {MonedasUsadas[3]} | 50 : {MonedasUsadas[4]} | 100 : {MonedasUsadas[5]}")    
        #Hay mas casos para el valor de regresion maximo?
        
        if count > 0:
            if MonedasUsadas[count] - 1  > 0:
                mascara[count] = 1
                MonedasUsadas[count] -= 1
                for x in range(len(MonedasDisp)):
                    MonedasUsadas[x] = MonedasUsadas[x] * mascara[x]
                Falta_por_Pagar = Quiero_cambiar - MonedasUsadas[count]*MonedasDisp[count]
                mascara = mascara = [0] * len(MonedasDisp)
                Regresion = count -1
            else: #count > 0 & MonedasUsadas[count] - 1 == 0:
                Regresion = count -1
                MonedasUsadas = [0] * len(MonedasDisp)
                Falta_por_Pagar = Quiero_cambiar
                count -= 1
        if count == 0:
            if Falta_por_Pagar == 0:    
                break
    
#print(f"{valor_max} y {count}")