# importo módulos desde la biblioteca estándar

# leer y escribir archivos parecidosa unahoja de cálculo
import csv

# crear nros aleatorios
import random

# manipular archivos en este caso los csv
import os

"""Utilizo la platilla para crear el objeto Niñera donde tambien se van a generar de acuerdo a los datos añadidos, archivos csv listando las niñeras de acuerdo a sus atributos"""


class Niñera:
    # atributo define el valor del precio por hora trabajada
    precio_por_hora = 3000

    # constructor y sus parámetros
    def __init__(self, nombre, apellido, horas_trabajadas):
        # inicializan los atributos privados de la instancia
        self._nombre = nombre
        self._apellido = apellido
        self._horas_trabajadas = horas_trabajadas

    @property  # decorador para convierte los métodos en getter para los atributos privados
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def horas_trabajadas(self):
        return self._horas_trabajadas

    @horas_trabajadas.setter
    def horas_trabajadas(self, horas):
        self._horas_trabajadas = horas


# Listas de nombres y apellidos para armar los CSV
nombres = [
    "Ana",
    "Andrea",
    "Belén",
    "Beatriz",
    "Celeste",
    "Carla",
    "Daniela",
    "Diana",
    "Estela",
    "Elena",
    "Florencia",
    "Fernanda",
    "Gisela",
    "Gabriela",
    "Isabel",
    "Iris",
    "Julia",
    "Juana",
    "Karina",
    "Lorena",
    "Lucía",
    "Morena",
    "María",
    "Nerea",
    "Natalia",
    "Oriana",
    "Olivia",
    "Pamela",
    "Patricia",
    "Rita",
    "Rosa",
    "Soledad",
    "Sandra",
    "Tiana",
    "Teresa",
    "Uma",
    "Úrsula",
    "Violeta",
    "Valeria",
    "Wanda",
    "Wendy",
    "Xiara",
    "Ximena",
    "Yolanda",
    "Yesica",
    "Zulma",
    "Zaira",
]
apellidos = [
    "Alvarez",
    "Araoz",
    "Blaz",
    "Blanco",
    "Corbalan",
    "Cruz",
    "Dominguez",
    "Díaz",
    "Ermes",
    "Estrada",
    "Flores",
    "Fernández",
    "Gomez",
    "García",
    "Hilton",
    "Hernández",
    "Iglesias",
    "Istas",
    "Jiménez",
    "Juarez",
    "Kroz",
    "Klein",
    "Ledesma",
    "López",
    "Mendez",
    "Martínez",
    "Nil",
    "Navarro",
    "Orson",
    "Ochoa",
    "Paez",
    "Pérez",
    "Quintana",
    "Quiroga",
    "Ruiz",
    "Ramírez",
    "Salto",
    "Sánchez",
    "Tomas",
    "Torres",
    "Uriarte",
    "Uribe",
    "Viaña",
    "Vargas",
    "Williams",
    "Wilson",
    "Xen",
    "Ximénez",
    "Yáñez",
    "Yos",
    "Zúñiga",
    "Zarate",
]


def limpiar_carpeta(carpeta):
    try:
        # bucle for para iterar sobre los archivos de la carpeta
        for archivo in os.listdir(carpeta):
            # para obtener la ruta completa del archivo
            archivo_path = os.path.join(carpeta, archivo)

            # la verifica
            if os.path.isfile(archivo_path):
                # lo elimina
                os.remove(archivo_path)

                # mediante el try capturo la excepción si ocurre un error lo muestra
    except Exception as e:
        print(f"Error al limpiar la carpeta '{carpeta}': {e}")


def generar_csv_por_dia(cantidad_dias):
    # Crear carpeta "temp" si no existe para evitar algún error
    carpeta_temporal = "temp"

    # verificasi existe la carpeta
    if not os.path.exists(carpeta_temporal):
        # la crea
        os.makedirs(carpeta_temporal)

    # Limpiar la carpeta "temp"
    limpiar_carpeta(carpeta_temporal)

    archivos_creados = []

    # mediante la función range itero sobreel rangode días
    for dia in range(1, cantidad_dias + 1):
        # Cantidad aleatoria de personas entre 1 y 10
        cantidad_registros = random.randint(1, 10)

        # genera una lista de nombres, apellidos y horas aleatorios conlos datos definidos para crear los csv
        datos = [
            (random.choice(nombres), random.choice(apellidos), random.randint(1, 8))
            for _ in range(cantidad_registros)
        ]

        # le defino el nombre que va a tener el archivo
        nombre_archivo = os.path.join(carpeta_temporal, f"Listado_Día{dia}.csv")

        # para abrir el archivo CSV y escribir en el
        with open(nombre_archivo, "w", newline="") as archivo_csv:
            # lo crea
            escritor_csv = csv.writer(archivo_csv)

            # Escribe los encabezados
            escritor_csv.writerow(["Nombre", "Apellido", "Horas Disponibles"])

            # Escribe los datos
            escritor_csv.writerows(datos)

        # función append() agrego un csv nuevo a los archivos creados al final delalista en la carpeta temporal
        archivos_creados.append(nombre_archivo)

    # devuelve los archivos creados
    return archivos_creados
