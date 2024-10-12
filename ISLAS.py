Tierra =    [[1,  0,  1, 1], #Establecer la matriz a analizar
            [1,  0,  1, 1], 
            [1,  1,  1, 1], 
            [1,  0,  1, 1]]

No_filas = len(Tierra) #Guarda el numero de filas en una variable 
No_columnas = len(Tierra[0]) #Guarda el numero de columnas en una variable 
#Se crea una matriz auxiliar en la cual todas sus celdas contienen "False" para guardar las coordenadas que contienenen islas 
zona_visitada = [[False for _ in range(No_columnas)] for _ in range(No_filas)]
num_islas = 0 #Variable que guarda el numero de islas
i = 0 #Inicia la variable i = 0 para desplazarse por filas 
while i < No_filas: #Ciclo para desplazarse por fila 
    j = 0 #Inicia la variable i = 0 para desplazarse por columnas
    while j < No_columnas: #Ciclo para desplazarse por columna
        #Si se encuentra una celda no visitada, es el comienzo de una nueva isla
        if Tierra[i][j] >= 1 and not zona_visitada[i][j]:
            #Marcar esta posición como visitada
            zona_visitada[i][j] = True
            num_islas += 1  #suma 1 al contador de islas
            #Se inicia una lista que guardará las coordenadas por visitar
            Lista_Ex = [[i, j]]
            #Variable auxiliar que se utilizará para buscar todas las zonas/celdas
            #que formen parte de una sola isla
            num_Ex = 0
            #Inicia el ciclo que buscará todas las zonas/celdas que forman parte de una sola isla
            while num_Ex < len(Lista_Ex): 
                
                # Obtener la coordenada del vecino actual
                x = Lista_Ex[num_Ex][0]
                y = Lista_Ex[num_Ex][1]
                
                # Revisar celdas vecinas (arriba, abajo, izquierda, derecha)

                # Abajo
                if x + 1 < No_filas and Tierra[x + 1][y] == 1 and not zona_visitada[x + 1][y]:
                    zona_visitada[x + 1][y] = True
                    Lista_Ex.append([x + 1, y])

                # Arriba
                if x - 1 >= 0 and Tierra[x - 1][y] == 1 and not zona_visitada[x - 1][y]:
                    zona_visitada[x - 1][y] = True
                    Lista_Ex.append([x - 1, y])

                # Derecha
                if y + 1 < No_columnas and Tierra[x][y + 1] == 1 and not zona_visitada[x][y + 1]:
                    zona_visitada[x][y + 1] = True
                    Lista_Ex.append([x, y + 1])

                # Izquierda
                if y - 1 >= 0 and Tierra[x][y - 1] == 1 and not zona_visitada[x][y - 1]:
                    zona_visitada[x][y - 1] = True
                    Lista_Ex.append([x, y - 1])
                
                # Incrementar el índice del vecino para seguir procesando la lista
                num_Ex += 1
        
        # Moverse a la siguiente columna
        j += 1
    # Moverse a la siguiente fila
    i += 1

# Imprimir el número de islas encontradas
print(f"Muestra contiene {num_islas} isla(s)")
