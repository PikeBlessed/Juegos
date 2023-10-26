import random

class Ruleta:
    @staticmethod
    def crear_opcion(numero_ganador):
        if numero_ganador == 0:
            return 'verde'
        elif numero_ganador in (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35):
            return 'negro'
        else:
            return 'rojo'
    @staticmethod
    def girar_ruleta():
        numero_ganador = 5 #random.randint(0, 36)
        return numero_ganador

    def obtener_opcion_valida(mensaje, opciones_validas):
        while True:
            opcion = input(mensaje).strip().lower()
            if opcion.isdigit() and int(opcion) in opciones_validas:
                return int(opcion)
            elif opcion in opciones_validas:
                return opcion
            else:
                print('Opcion invalida. Por favor, elige una opcion valida.')