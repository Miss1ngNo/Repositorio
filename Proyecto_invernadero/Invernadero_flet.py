import json
import os
import flet as ft

class SensorTemperatura:
    def __init__(self, temperatura_actual, temperatura_objetivo, temp_min, temp_max):
        self.temperatura_actual = temperatura_actual
        self.temperatura_objetivo = temperatura_objetivo
        self.limite_min = temp_min
        self.limite_max = temp_max

    def ajustar_temperatura(self, temperatura):
        if self.limite_min <= temperatura <= self.limite_max:
            self.temperatura_actual = temperatura
            self.temperatura_objetivo = temperatura
        else:
            print(f"La temperatura {temperatura} está fuera de los límites recomendados.")
                
class SensorHumedad:
    def __init__(self, humedad_actual, humedad_objetivo, humedad_min, humedad_max):
        self.humedad_actual = humedad_actual
        self.humedad_objetivo = humedad_objetivo
        self.limite_min = humedad_min
        self.limite_max = humedad_max

    def ajustar_humedad(self, humedad):
        if self.limite_min <= humedad <= self.limite_max:
            self.humedad_actual = humedad
            self.humedad_objetivo = humedad
        else:
            print(f"La humedad {humedad} está fuera de los límites recomendados.")
                
class ActuadorLuz:
    def __init__(self, luz_actual, luz_objetivo, luminosidad_min, luminosidad_max):
        self.luz_actual = luz_actual
        self.luz_objetivo = luz_objetivo
        self.limite_min = luminosidad_min
        self.limite_max = luminosidad_max

    def ajustar_luz(self, luminosidad):
        if self.limite_min <= luminosidad <= self.limite_max:
            self.luz_actual = luminosidad
            self.luz_objetivo = luminosidad
        else:
            print(f"La luminosidad {luminosidad} está fuera de los límites recomendados.")

class ControladorInvernadero: # 
    def __init__(self):
        self.sensor_temperatura = SensorTemperatura(20, 20, 10, 35) # Grados C
        self.sensor_humedad = SensorHumedad(60, 60, 60, 70) # %Humedad
        self.actuador_luz = ActuadorLuz(12000, 12000, 10000 , 20000)  # Luxes 
        
    def ajustar_variables(self, temperatura, humedad, luz):
        self.sensor_temperatura.temperatura_objetivo = temperatura
        self.sensor_humedad.humedad_objetivo = humedad
        self.actuador_luz.luz_objetivo = luz

    # Actualiza las variables con los valores proporcionados
        self.sensor_temperatura.ajustar_temperatura(temperatura)
        self.sensor_humedad.ajustar_humedad(humedad)
        self.actuador_luz.ajustar_luz(luz)


    def obtener_variables(self):
        return {
            "temperatura": self.sensor_temperatura.temperatura_actual,
            "humedad": self.sensor_humedad.humedad_actual,
            "luz": self.actuador_luz.luz_actual
        }

class ManejoArchivos:
    def __init__(self, archivo):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w') as f:
                json.dump([], f)

    def alta(self, datos):
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        registros.append(datos)
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def baja(self, indice):
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        if 0 <= indice < len(registros):
            registros.pop(indice)
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def modificar(self, indice, nuevos_datos):
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        if 0 <= indice < len(registros):
            registros[indice] = nuevos_datos
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def consultar(self):
        with open(self.archivo, 'r') as f:
            return json.load(f)

def main(page: ft.Page):
    invernadero = ControladorInvernadero()
    archivo = ManejoArchivos("variables.json")
    
    # Función para mostrar variables
    def mostrar_variables():
        variables = archivo.consultar()
        lista_variables.controls.clear()
        if variables:
            for i, pos in enumerate(variables):
                lista_variables.controls.append(ft.Text(f"Variables {i}: Temperatura={pos['temperatura']}, Humedad={pos['humedad']}, Luz={pos['luz']}"))
        else:
            lista_variables.controls.append(ft.Text("No hay variables guardadas."))
        limpiar_campos()
        page.update()

    # Función para limpiar campos de texto
    def limpiar_campos():
        temperatura.value = ""
        humedad.value = ""
        luz.value = ""
        indice_baja.value = ""
        indice_modificar.value = ""

    # Funciones de alta, baja y modificación
    def alta_click(e):
        try:
            var_temperatura = float(temperatura.value)
            var_humedad = float(humedad.value)
            var_luz = float(luz.value)
            invernadero.ajustar_variables(var_temperatura, var_humedad, var_luz)
            archivo.alta(invernadero.obtener_variables())
            resultado.value = "Variables guardada exitosamente."
            mostrar_variables()
        except ValueError:
            resultado.value = "Error: Ingrese valores numéricos válidos."
        page.update()

    def baja_click(e):
        try:
            indice = int(indice_baja.value)
            archivo.baja(indice)
            resultado.value = "Variables eliminada exitosamente."
            mostrar_variables()
        except ValueError:
            resultado.value = "Error: Ingrese un índice válido."
        page.update()

    def modificar_click(e):
        try:
            indice = int(indice_modificar.value)
            var_temperatura = float(temperatura.value)
            var_humedad = float(humedad.value)
            var_luz = float(luz.value)
            invernadero.ajustar_variables(var_temperatura, var_humedad, var_luz)
            archivo.modificar(indice, invernadero.obtener_variables())
            resultado.value = "Variables modificada exitosamente."
            mostrar_variables()
        except ValueError:
            resultado.value = "Error: Ingrese valores numéricos válidos."
        page.update()

    # Elementos de la interfaz
    temperatura = ft.TextField(label="Temperatura")
    humedad = ft.TextField(label="Humedad")
    luz = ft.TextField(label="Luminosidad")
    indice_baja = ft.TextField(label="Índice para eliminar")
    indice_modificar = ft.TextField(label="Índice para modificar")
    resultado = ft.Text()
    
    # Contenedor con scroll para las posiciones guardadas
    lista_variables = ft.Column(scroll="adaptive")

    # Menú de opciones
    def cambiar_vista(menu_item):
        container_opciones.controls.clear()
        resultado.value = ""
        if menu_item == "Alta":
            container_opciones.controls.extend([temperatura, humedad, luz, ft.ElevatedButton("Guardar Variables", on_click=alta_click)])
        elif menu_item == "Baja":
            container_opciones.controls.extend([indice_baja, ft.ElevatedButton("Eliminar Variables", on_click=baja_click)])
        elif menu_item == "Modificación":
            container_opciones.controls.extend([indice_modificar, temperatura, humedad, luz, ft.ElevatedButton("Modificar Variables", on_click=modificar_click)])
        elif menu_item == "Consultas":
            mostrar_variables()
        limpiar_campos()
        page.update()

    # Contenedor para los menús y opciones
    container_opciones = ft.Column()
    
    # Interfaz principal
    page.add(
        ft.Text("Control de Invernadero", style="headlineMedium"),
        ft.Row([ft.ElevatedButton(text="Alta", on_click=lambda e: cambiar_vista("Alta")),
                ft.ElevatedButton(text="Baja", on_click=lambda e: cambiar_vista("Baja")),
                ft.ElevatedButton(text="Modificación", on_click=lambda e: cambiar_vista("Modificación")),
                ft.ElevatedButton(text="Consultas", on_click=lambda e: cambiar_vista("Consultas"))]),
        container_opciones,
        resultado,
        ft.Text("Variables Guardadas:", style="headlineSmall"),
        lista_variables
    )

    # Inicializa con la lista de variables guardadas ajustar_variables
    mostrar_variables()

ft.app(target=main, view="web_browser")