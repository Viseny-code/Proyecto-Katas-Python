"""
PROYECTO KATAS PYTHON

Archivo principal con ejercicios resueltos.
"""

from functools import reduce


# KATA 1
# Crear una función que reciba una cadena y devuelva
# un diccionario con la frecuencia de cada letra.

def frecuencia_letras(texto):
    resultado = {}
    for letra in texto.lower():
        if letra != " ":
            resultado[letra] = resultado.get(letra, 0) + 1
    return resultado


# KATA 2
# Obtener una lista con el doble de cada número usando map()

def duplicar_lista(lista):
    return list(map(lambda x: x * 2, lista))


# KATA 3
# Buscar palabras que contienen una palabra objetivo

def buscar_palabras(lista, objetivo):
    return list(filter(lambda x: objetivo.lower() in x.lower(), lista))


# KATA 4
# Diferencia entre dos listas usando map()

def diferencia_listas(a, b):
    return list(map(lambda x: x[0]-x[1], zip(a, b)))


# KATA 5
# Calcular media y estado aprobado/suspenso

def evaluar_nota(notas, nota_aprobado=5):
    media = sum(notas)/len(notas)
    return (media, "aprobado" if media >= nota_aprobado else "suspenso")


# KATA 6
# Factorial recursivo

def factorial(numero):
    if numero <= 1:
        return 1
    return numero * factorial(numero-1)


# KATA 7
# Convertir lista de tuplas a strings

def convertir_tuplas(datos):
    return list(map(str, datos))


# KATA 8
# División controlando errores

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir entre cero"


# KATA 9
# Filtrar mascotas prohibidas

def filtrar_mascotas(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda x: x not in prohibidas, mascotas))


# KATA 10
# Excepción personalizada para lista vacía

class ListaVaciaError(Exception):
    pass


def promedio(lista):
    if not lista:
        raise ListaVaciaError("Lista vacía")
    return sum(lista)/len(lista)


# KATA 34
# Clase Arbol

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
            "ramas": self.ramas
        }


# Ejemplo de ejecución

if __name__ == "__main__":
    print(frecuencia_letras("Python"))
    print(duplicar_lista([1,2,3]))

    arbol = Arbol()
    arbol.nueva_rama()
    arbol.crecer_tronco()
    print(arbol.info_arbol())
