import json
import os
import flet as ft

class Articulacion:
    def __init__(self, angulo_actual, angulo_objetivo, velocidad, limite_min, limite_max):
        self.angulo_actual = angulo_actual
        self.angulo_objetivo = angulo_objetivo
        self.velocidad = velocidad
        self.limite_min = limite_min
        self.limite_max = limite_max

    def set_angulo(self, angulo):
        if self.limite_min <= angulo <= self.limite_max:
            self.angulo_actual = angulo
            self.angulo_objetivo = angulo
        else:
            print(f"El ángulo {angulo} está fuera de los límites para esta articulación.")

class BrazoRobotico:
    def __init__(self):
        self.hombro = Articulacion(0, 0, 1, -90, 90)
        self.codo = Articulacion(0, 0, 1, 0, 135)
        self.muneca = Articulacion(0, 0, 1, -90, 90)
        self.pinza = Articulacion(0, 0, 1, 0, 180)

    def mover_a_posicion(self, posiciones_objetivo):
        self.hombro.set_angulo(posiciones_objetivo[0])
        self.codo.set_angulo(posiciones_objetivo[1])
        self.muneca.set_angulo(posiciones_objetivo[2])
        self.pinza.set_angulo(posiciones_objetivo[3])

    def obtener_posiciones(self):
        return {
            "hombro": self.hombro.angulo_actual,
            "codo": self.codo.angulo_actual,
            "muneca": self.muneca.angulo_actual,
            "pinza": self.pinza.angulo_actual
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
    brazo = BrazoRobotico()
    archivo = ManejoArchivos("articulaciones.json")
    
    # Función para mostrar posiciones
    def mostrar_posiciones():
        posiciones = archivo.consultar()
        lista_posiciones.controls.clear()
        if posiciones:
            for i, pos in enumerate(posiciones):
                lista_posiciones.controls.append(ft.Text(f"Posición {i}: Hombro={pos['hombro']}, Codo={pos['codo']}, Muñeca={pos['muneca']}, Pinza={pos['pinza']}"))
        else:
            lista_posiciones.controls.append(ft.Text("No hay posiciones guardadas."))
        limpiar_campos()
        page.update()

    # Función para limpiar campos de texto
    def limpiar_campos():
        hombro.value = ""
        codo.value = ""
        muneca.value = ""
        pinza.value = ""
        indice_baja.value = ""
        indice_modificar.value = ""

    # Funciones de alta, baja y modificación
    def alta_click(e):
        try:
            pos_hombro = float(hombro.value)
            pos_codo = float(codo.value)
            pos_muneca = float(muneca.value)
            pos_pinza = float(pinza.value)
            brazo.mover_a_posicion([pos_hombro, pos_codo, pos_muneca, pos_pinza])
            archivo.alta(brazo.obtener_posiciones())
            resultado.value = "Posición guardada exitosamente."
            mostrar_posiciones()
        except ValueError:
            resultado.value = "Error: Ingrese valores numéricos válidos."
        page.update()

    def baja_click(e):
        try:
            indice = int(indice_baja.value)
            archivo.baja(indice)
            resultado.value = "Posición eliminada exitosamente."
            mostrar_posiciones()
        except ValueError:
            resultado.value = "Error: Ingrese un índice válido."
        page.update()

    def modificar_click(e):
        try:
            indice = int(indice_modificar.value)
            pos_hombro = float(hombro.value)
            pos_codo = float(codo.value)
            pos_muneca = float(muneca.value)
            pos_pinza = float(pinza.value)
            brazo.mover_a_posicion([pos_hombro, pos_codo, pos_muneca, pos_pinza])
            archivo.modificar(indice, brazo.obtener_posiciones())
            resultado.value = "Posición modificada exitosamente."
            mostrar_posiciones()
        except ValueError:
            resultado.value = "Error: Ingrese valores numéricos válidos."
        page.update()

    # Elementos de la interfaz
    hombro = ft.TextField(label="Ángulo del hombro")
    codo = ft.TextField(label="Ángulo del codo")
    muneca = ft.TextField(label="Ángulo de la muñeca")
    pinza = ft.TextField(label="Ángulo de la pinza")
    indice_baja = ft.TextField(label="Índice para eliminar")
    indice_modificar = ft.TextField(label="Índice para modificar")
    resultado = ft.Text()
    
    # Contenedor con scroll para las posiciones guardadas
    lista_posiciones = ft.Column(scroll="adaptive")

    # Menú de opciones
    def cambiar_vista(menu_item):
        container_opciones.controls.clear()
        resultado.value = ""
        if menu_item == "Alta":
            container_opciones.controls.extend([hombro, codo, muneca, pinza, ft.ElevatedButton("Guardar Posición", on_click=alta_click)])
        elif menu_item == "Baja":
            container_opciones.controls.extend([indice_baja, ft.ElevatedButton("Eliminar Posición", on_click=baja_click)])
        elif menu_item == "Modificación":
            container_opciones.controls.extend([indice_modificar, hombro, codo, muneca, pinza, ft.ElevatedButton("Modificar Posición", on_click=modificar_click)])
        elif menu_item == "Consultas":
            mostrar_posiciones()
        limpiar_campos()
        page.update()

    # Contenedor para los menús y opciones
    container_opciones = ft.Column()
    
    # Interfaz principal
    page.add(
        ft.Text("Control de Brazo Robótico", style="headlineMedium"),
        ft.Row([ft.ElevatedButton(text="Alta", on_click=lambda e: cambiar_vista("Alta")),
                ft.ElevatedButton(text="Baja", on_click=lambda e: cambiar_vista("Baja")),
                ft.ElevatedButton(text="Modificación", on_click=lambda e: cambiar_vista("Modificación")),
                ft.ElevatedButton(text="Consultas", on_click=lambda e: cambiar_vista("Consultas"))]),
        container_opciones,
        resultado,
        ft.Text("Posiciones Guardadas:", style="headlineSmall"),
        lista_posiciones
    )

    # Inicializa con la lista de posiciones guardadas
    mostrar_posiciones()

ft.app(target=main, view="web_browser")