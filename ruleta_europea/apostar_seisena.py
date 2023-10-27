from ruleta_opciones import Ruleta

class Seisena:

    def apostar_seisena(dinero_disponible, numero_ganador):
        seisena_elegida = Ruleta.obtener_opcion_valida('Elige la seisena a la que desea apostar (1, 2, 3, 4, 5, 6): ', [1, 2, 3, 4, 5, 6])
        dinero_apostado = int(input('Ingrese la cantidad a apostar: '))


        dinero_ganado = 0
        dinero_perdido = 0
        if dinero_apostado > dinero_disponible:
            print("No puedes apostar más dinero del que tienes disponible.")
            return dinero_disponible, 0, 0
        else:
            if (seisena_elegida == 1 and numero_ganador in range(1, 7)) or \
            (seisena_elegida == 2 and numero_ganador in range(7, 13)) or \
            (seisena_elegida == 3 and numero_ganador in range(13, 19)) or \
            (seisena_elegida == 4 and numero_ganador in range(19, 25)) or \
            (seisena_elegida == 5 and numero_ganador in range(25, 31)) or \
            (seisena_elegida == 6 and numero_ganador in range(31, 37)):
                dinero_ganado = dinero_apostado * 6
            else:
                dinero_perdido -= dinero_apostado

        return dinero_disponible, dinero_ganado, dinero_perdido