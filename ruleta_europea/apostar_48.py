from ruleta_opciones import Ruleta


class CuarentaPorciento:
    
    def apostar_color(dinero_disponible, numero_ganador):
        color_elegido = Ruleta.obtener_opcion_valida('Elige el color al que quieres apostar (rojo, negro o verde): ', ['rojo', 'negro', 'verde'])
        dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

        color_ganador = Ruleta.crear_opcion(numero_ganador)

        dinero_ganado = 0
        dinero_perdido = 0
        if dinero_apostado > dinero_disponible:
            print("No puedes apostar más dinero del que tienes disponible.")
            return dinero_disponible, 0, 0
        else:
            if color_elegido == color_ganador:
                if color_ganador == 'verde':
                    dinero_ganado = dinero_apostado * 36
                else:
                    dinero_ganado = dinero_apostado * 2
            else:
                dinero_perdido -= dinero_apostado

        return dinero_disponible, dinero_ganado, dinero_perdido

    def apostar_par_impar(dinero_disponible, numero_ganador):
        par_impar_elegido = Ruleta.obtener_opcion_valida('Elige si quieres apostar a un número par o impar: ', ['par', 'impar'])
        dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

        dinero_ganado = 0
        dinero_perdido = 0
        if dinero_apostado > dinero_disponible:
            print("No puedes apostar más dinero del que tienes disponible.")
            return dinero_disponible, 0, 0
        else:
            if par_impar_elegido == 'par':
                if numero_ganador % 2 == 0:
                    dinero_ganado = dinero_apostado * 2
                else:
                    dinero_perdido -= dinero_apostado
            elif par_impar_elegido == 'impar':
                if numero_ganador % 2 == 1:
                    dinero_ganado = dinero_apostado * 2
                else:
                    dinero_perdido -= dinero_apostado

        return dinero_disponible, dinero_ganado, dinero_perdido
            

    def apostar_falta_pasa(dinero_disponible, numero_ganador):
        falta_pasa_elegido = Ruleta.obtener_opcion_valida('Elige falta o pasa: ', ['falta', 'pasa'])
        dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

        dinero_ganado = 0
        dinero_perdido = 0
        if dinero_apostado > dinero_disponible:
            print("No puedes apostar más dinero del que tienes disponible.")
            return dinero_disponible, 0, 0
        else:
            if falta_pasa_elegido == 'falta':
                if numero_ganador in range(1, 19):
                    dinero_ganado = dinero_apostado * 2
                else:
                    dinero_disponible -= dinero_apostado
            elif falta_pasa_elegido == 'pasa':
                if numero_ganador in range(19, 37):
                    dinero_ganado = dinero_apostado * 2
                else:
                    dinero_perdido -= dinero_apostado

        return dinero_disponible, dinero_ganado, dinero_perdido