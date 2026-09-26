"""
PROYECTO LÓGICA: KATAS DE PYTHON

Archivo principal con la resolución de las katas del proyecto.
Cada ejercicio aparece identificado con su comentario.
"""

from functools import reduce


# KATA 1
# Función que cuenta la frecuencia de letras de una cadena ignorando espacios.
def frecuencia_letras(texto):
    resultado = {}
    for letra in texto.lower():
        if letra != " ":
            resultado[letra] = resultado.get(letra, 0) + 1
    return resultado


# KATA 2
# Obtener una lista con el doble de cada valor usando map().
def duplicar_valores(lista):
    return list(map(lambda x: x * 2, lista))


# KATA 3
# Obtener palabras que contienen una palabra objetivo.
def palabras_contienen(lista, objetivo):
    return list(filter(lambda x: objetivo.lower() in x.lower(), lista))


# KATA 4
# Diferencia entre dos listas usando map().
def diferencia_listas(lista1, lista2):
    return list(map(lambda x: x[0] - x[1], zip(lista1, lista2)))


# KATA 5
# Calcular media y estado aprobado/suspenso.
def evaluar_notas(notas, nota_aprobado=5):
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado


# KATA 6
# Factorial mediante recursividad.
def factorial(numero):
    if numero <= 1:
        return 1
    return numero * factorial(numero - 1)


# KATAS 7-33
# Funciones adicionales del proyecto trabajadas con estructuras,
# lambda, filter, reduce y excepciones.

def convertir_tuplas(lista):
    return list(map(str, lista))


def producto_lista(lista):
    return reduce(lambda a, b: a*b, lista)


def concatenar_palabras(lista):
    return reduce(lambda a, b: a + " " + b, lista)


class ListaVaciaError(Exception):
    pass


def promedio(lista):
    if not lista:
        raise ListaVaciaError("La lista está vacía")
    return sum(lista)/len(lista)


# KATA 34
# Clase Arbol con tronco y ramas.
class Arbol:

    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        self.ramas.pop(posicion)

    def info_arbol(self):
        return {
            "tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitud_ramas": self.ramas
        }


# KATA 36
# Clase UsuarioBanco para gestionar usuarios y saldo.
class UsuarioBanco:

    def __init__(self, nombre, saldo, cuenta_corriente=True):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        otro_usuario.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)


# KATAS 37-41
# Funciones finales del proyecto.

def contar_palabras(texto):
    palabras = texto.split()
    resultado = {}
    for palabra in palabras:
        resultado[palabra] = resultado.get(palabra, 0) + 1
    return resultado


def clasificar_nota(nota):
    if nota < 70:
        return "insuficiente"
    elif nota < 80:
        return "bien"
    elif nota < 90:
        return "muy bien"
    else:
        return "excelente"


def cubo(numero):
    return numero ** 3


if __name__ == "__main__":
    print("Proyecto Katas Python ejecutado correctamente")
    print(frecuencia_letras("Python"))
    arbol = Arbol()
    arbol.nueva_rama()
    print(arbol.info_arbol())
