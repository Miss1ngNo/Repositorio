# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 23:03:56 2024

@author: angel
"""

# Se crea una lista de los valores de moneda disponible
monedas_disp = [1, 5, 10, 20, 50, 100]

# Se declara el valor de la cantidad a cambiar 
quiero_cambiar = 100

def encontrar_combinaciones(quiero_cambiar, monedas_disp):
    # Función que encuentra todas las combinaciones de monedas para la cantidad dada
    def buscar(quiero_cambiar, monedas_disp, indice, combinacion_actual, todas_combinaciones):
        if quiero_cambiar == 0:
            todas_combinaciones.append(combinacion_actual[:])
            return
        if quiero_cambiar < 0 or indice >= len(monedas_disp):
            return
        
        # Opción 1: Incluir la moneda actual
        combinacion_actual[indice] += 1
        buscar(quiero_cambiar - monedas_disp[indice], monedas_disp, indice, combinacion_actual, todas_combinaciones)
        
        # Opción 2: No incluir la moneda actual y pasar a la siguiente
        combinacion_actual[indice] -= 1
        buscar(quiero_cambiar, monedas_disp, indice + 1, combinacion_actual, todas_combinaciones)

    todas_combinaciones = []
    combinacion_actual = [0] * len(monedas_disp)
    buscar(quiero_cambiar, monedas_disp, 0, combinacion_actual, todas_combinaciones)
    
    return todas_combinaciones

# Llamamos a la función para encontrar todas las combinaciones posibles
combinaciones = encontrar_combinaciones(quiero_cambiar, monedas_disp)

# Imprimimos los resultados
for i, combinacion in enumerate(combinaciones):
    print(f"{i + 1}: {combinacion}")
