# Ejercicio 1: PEP8

# MAL CODIGO
import logging

def calcular_aerea(base, altura):
    res=base*altura
    print(res)
    return res

# CODIGO DE CALIDAD
def calcular_area(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo."""
    if base < 0 or altura < 0:
        raise ValueError("base y altura deben ser no-negativos")
    return base * altura


# Ejercicio 2: 

# MAL CODIGO

def obtener_dia(n):
    if n == 1:
        return "Lunes"
    elif n == 2:
        return "Martes"
    elif n == 3:
        return "Miércoles"
    elif n == 4:
        return "Jueves"
    elif n == 5:
        return "Viernes"
    else:
        return "Día no válido"

# CODIGO DE CALIDAD

def obtener_nombre_dia(dia_idx: int) -> str:
    dias = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes"}
    return dias.get(dia_idx, "Día no válido")


# Ejercicio 3: 

# MAL CODIGO
try:
    valor = 10 / 0
except:
    pass

# CODIGO DE CALIDAD
try:
    valor = 10 / 0
except ZeroDivisionError as e:
    logging.error("Error de división: %s", e)
    valor = None


# Ejercicio 4: 

# MAL CODIGO
class Reporte:
    def ejecutar(self):
        datos = self.leer_datos()
        metricas = self.calcular_metricas(datos)
        self.generar_pdf(metricas)

    def leer_datos(self):
        pass

    def calcular_metricas(self, datos):
        pass

    def generar_pdf(self, metricas):
        pass

# CODIGO DE CALIDAD
class LectorDeDatos:
    def leer(self):
        pass

class CalculadorDeMetricas:
    def calcular(self, datos):
        pass

class GeneradorDeReporte:
    def generar(self, metricas):
        pass


# Ejercicio 5: 

# MAL CODIGO
API_KEY = "SECRET_12345"

# CODIGO DE CALIDAD
import os

def obtener_api_key() -> str:
    return os.getenv("API_KEY_SERVICE", "valor_por_defecto_seguro")


# Ejercicio 6: 

# MAL CODIGO

def procesar_usuarios(usuarios):
    return {u: len(u) for u in usuarios}

# CODIGO DE CALIDAD
from typing import List, Dict

def procesar_usuarios_typed(usuarios: List[str]) -> Dict[str, int]:
    return {u: len(u) for u in usuarios}


# Ejercicio 7:  

# MAL CODIGO

def formato_precio1(valor):
    return f"${valor:,.2f}"

# CODIGO DE CALIDAD

def formatear_moneda(valor: float) -> str:
    return f"${valor:,.2f}"


# Ejercicio 8: 

# MAL CODIGO

def enviar_email(destino, asunto):
    pass

# CODIGO DE CALIDAD

def enviar_email_doc(destino: str, asunto: str) -> None:
    """Envía un correo electrónico.

    Args:
        destino (str): Correo del receptor.
        asunto (str): Título del mensaje.
    """
    pass


# Ejercicio 9:  

# MAL CODIGO

def leer_archivo_entero(ruta):
    with open(ruta, 'r') as f:
        return f.readlines()

# CODIGO DE CALIDAD

def leer_archivo_gigante(ruta: str):
    with open(ruta, 'r') as f:
        for linea in f:
            yield linea.strip()


# Ejercicio 10:  

# MAL CODIGO

# resultado = eval(input("Suma: "))

# CODIGO DE CALIDAD
import ast

def evaluar_expresion_segura(entrada: str):
    if entrada.isdigit():
        return ast.literal_eval(entrada)
    return "Error"


if __name__ == "__main__":
    print(calcular_area(5, 3))
    print(obtener_nombre_dia(2))
    print(valor)
    print(obtener_api_key())
    print(procesar_usuarios_typed(["ana", "pedro"]))
    print(formatear_moneda(1234.56))
    print(evaluar_expresion_segura("5"))