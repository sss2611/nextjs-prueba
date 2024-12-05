import csv
from src.model.NiñerasModel import Niñera, generar_csv_por_dia
from src.view.NiñerasView import NiñerasView

class NiñerasController:

    def __init__(self):
        self.niñeras_por_dia = {}
        self.vista = NiñerasView()

    def agregar_niñera(self, dia, nombre, apellido, horas_trabajadas):
        if dia not in self.niñeras_por_dia:
            self.niñeras_por_dia[dia] = []
        niñera = Niñera(nombre, apellido, horas_trabajadas)
        niñera.cobrado_por_horas = self.calcular_cobrado_por_horas(niñera)
        niñera.descuento = self.calcular_descuento(niñera)
        niñera.pago_neto_por_jornada = self.calcular_ganancia(niñera)
        self.niñeras_por_dia[dia].append(niñera)

    def calcular_cobrado_por_horas(self, niñera):
        return niñera.horas_trabajadas * Niñera.precio_por_hora

    def calcular_descuento(self, niñera):
        return niñera.cobrado_por_horas * 0.1 

    def calcular_ganancia(self, niñera):
        return niñera.cobrado_por_horas - niñera.descuento

    def calcular_descuento_dia(self, dia):
        return sum(niñera.descuento for niñera in self.niñeras_por_dia[dia])

    def calcular_ganancia_total(self):
        return sum(self.calcular_ganancia_dia(dia) for dia in self.niñeras_por_dia)

    def calcular_ganancia_dia(self, dia):
        return sum(niñera.descuento for niñera in self.niñeras_por_dia[dia])

    def mostrar_niñeras_por_dia(self, dia):
        for niñera in self.niñeras_por_dia[dia]:
            self.vista.mostrar_niñera(niñera)

    def ejecutar(self):
        cantidad_dias = self.vista.solicitar_cantidad_dias()
        generar_csv_por_dia(cantidad_dias)

        for dia in range(1, cantidad_dias + 1):
            input("Presiona 'Enter' para ver más ...\n")
            archivo = f'temp/Listado_Día{dia}.csv'
            niñeras_dia = []
            with open(archivo, 'r') as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                next(lector_csv)  # Saltar la fila de encabezado
                for fila in lector_csv:
                    nombre, apellido, horas_trabajadas = fila
                    self.agregar_niñera(dia, nombre, apellido, int(horas_trabajadas))
                    niñeras_dia.append(self.niñeras_por_dia[dia][-1])  # Añadir la última niñera agregada
            self.vista.mostrar_niñeras_por_dia(dia, niñeras_dia)
            ganancia_dia = self.calcular_ganancia_dia(dia)
            self.vista.mostrar_ganancia_dia(dia, ganancia_dia)

        ganancia_total = self.calcular_ganancia_total()
        self.vista.mostrar_ganancia_total(ganancia_total, cantidad_dias)
