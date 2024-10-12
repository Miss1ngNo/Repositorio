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

#Declaramos un entero que disminuira el valor de las monedas utilizadas
Regresion = len(MonedasDisp) - 1

caso = 0

while 1:
    
    if Falta_por_Pagar >= MonedasDisp[Regresion]:
        Falta_por_Pagar -= MonedasDisp[Regresion]
        MonedasUsadas[Regresion] += 1 
    else:
        Regresion -= 1
    if Falta_por_Pagar == 0:
        caso +=1
        break
print(f"Caso {caso}, monedas usadas de: 1 : {MonedasUsadas[0]} | 5 : {MonedasUsadas[1]} | 10 : {MonedasUsadas[2]} | 20 : {MonedasUsadas[3]} | 50 : {MonedasUsadas[4]} | 100 : {MonedasUsadas[5]}")    
        