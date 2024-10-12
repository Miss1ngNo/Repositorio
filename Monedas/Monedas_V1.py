# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 23:03:56 2024

@author: angel
"""

#Se crea una lista de los valores de moneda disponible y una lista 
#del mismo tamaño que guardada la cantidad utilizada de cada moneda
MonedasDisp = [1, 5, 10, 20, 50, 100]
MonedasUsadas = [0] * len(MonedasDisp)

#Se declara el valor de la moneda a cambiar 
Quiero_cambiar = 50
Falta_por_Pagar = Quiero_cambiar

while 1:
    if Quiero_cambiar >= MonedasDisp[4]:
        Falta_por_Pagar -= MonedasDisp[4]
        MonedasUsadas[4] += 1 
    if Falta_por_Pagar == 0:
        break
print(f"monedas usadas de: 1 : {MonedasUsadas[0]} | 5 : {MonedasUsadas[1]} | 10 : {MonedasUsadas[2]} | 20 : {MonedasUsadas[3]} | 50 : {MonedasUsadas[4]} | 100 : {MonedasUsadas[5]}")    
        