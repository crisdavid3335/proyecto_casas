class Comprador:
    def __init__(self, edad, ocupacion, barrio_preferencia, lugar_vivienda_actual, ingreso_mensual, tamano_familia):
        self.edad = edad
        self.ocupacion = ocupacion
        self.barrio_preferencia = barrio_preferencia
        self.lugar_vivienda_actual = lugar_vivienda_actual
        self.ingreso_mensual = ingreso_mensual
        self.tamano_familia = tamano_familia

    def __str__(self):
        return f"Comprador: Edad: {self.edad}, Ocupación: {self.ocupacion}, Barrio Preferencia: {self.barrio_preferencia}, Lugar Vivienda Actual: {self.lugar_vivienda_actual}, Ingreso Mensual: {self.ingreso_mensual}, Tamaño Familia: {self.tamano_familia}"
