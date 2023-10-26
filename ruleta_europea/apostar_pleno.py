from ruleta_opciones import Ruleta


numeros = list(range(0, 37))
class Pleno:
    def apostar_numero(dinero_disponible, numero_ganador):
        numero_elegido = Ruleta.obtener_opcion_valida('Ingrese el número al que desea apostar(0, 36): ', list(numeros))
        dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

        dinero_ganado = 0

        if numero_ganador == numero_elegido:
            dinero_ganado = dinero_apostado * 36
            dinero_disponible += dinero_ganado
        else:
            dinero_disponible -= dinero_apostado

        return dinero_disponible, dinero_ganado, dinero_apostado
