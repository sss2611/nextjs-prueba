class NiñerasView:

    def __init__(self):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+                        PROGRAMACIÓN I ITSE2024                        +")
        print("+                            MESA: 10/12                                +")
        print("+                                                                       +")
        print("+                           NIÑERAS POR HORAS                           +")
        print("+                           SANDRA S. SANCHEZ                           +")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    def solicitar_cantidad_dias(self):
        while True:
            try:
                cantidad_dias = int(input("\nCuántos días de esta semana que quieres consultar? \n"))
                if 1 <= cantidad_dias <= 7:
                    return cantidad_dias
                else:
                    print("Por favor, ingresa un número entre 1 y 7.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número válido.")
            

    def mostrar_niñera(self, niñera):
        print(f"\n{niñera.nombre} {niñera.apellido}, Horas trabajadas: {niñera.horas_trabajadas}, Total = ${niñera.cobrado_por_horas:.2f}, Descuento = ${niñera.descuento:.2f}, Pago Neto por Jornada: ${niñera.pago_neto_por_jornada:.2f}")


    def mostrar_ganancia_dia(self, dia, ganancia_dia):
        print(f"Ganancia del día {dia}: ${ganancia_dia:.2f}")
        print("\n***************************************************")

    def mostrar_niñeras_por_dia(self, dia, niñeras):
        print(f"\nListado de niñeras del día {dia}:")
        print("--------------------------------")
        for niñera in niñeras:
            self.mostrar_niñera(niñera)
        print("\n***************************************************")
        print(f"\nCantidad de Niñeras que trabajaron: {len(niñeras)}")
      

    def mostrar_ganancia_total(self, ganancia_total, cantidad_dias):
        print(f"\nGanancia Total de los {cantidad_dias} días: ${ganancia_total:.2f}")
        print("\n***************************************************")