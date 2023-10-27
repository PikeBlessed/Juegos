from ruleta_opciones import Ruleta


caballos = {'1-2': [1, 2], '1-4': [1, 4], '2-3': [2, 3], '2-5': [2, 5], '3-6': [3, 6], '4-5': [4, 5], '4-7': [4, 7], '5-6': [5, 6], '5-8': [5, 8], '6-9': [6, 9], '7-8': [7, 8], '7-10': [7, 10], '8-9': [8, 
    9], '8-11': [8, 11], '9-12': [9, 12], '10-11': [10, 11], '10-13': [10, 13], '11-12': [11, 12], '11-14': [11, 14], '12-15': [12, 15], '13-14': [13, 14], '13-16': [13, 16], '14-15': [14, 15], '14-17': [14, 17], '15-18': [15, 18], '16-17': [16, 17], '16-19': [16, 19], '17-18': [17, 18], '17-20': [17, 20], '18-21': [18, 21], '19-20': [19, 20], '19-22': [19, 22], '20-21': [20, 21], '20-23': [20, 23], '21-24': [21, 24], '22-23': [22, 23], '22-25': [22, 25], '23-24': [23, 24], '23-26': [23, 26], '24-27': [24, 27], '25-26': [25, 26], '25-28': [25, 28], '26-27': [26, 27], '26-29': [26, 29], '27-30': [27, 30], '28-29': [28, 29], '28-31': [28, 31], '29-30': [29, 30], '29-32': [29, 
    32], '30-33': [30, 33], '31-32': [31, 32], '31-34': [31, 34], '32-33': [32, 33], '32-35': [32, 35], '33-36': [33, 36], '34-35': [34, 35], '35-36': [35, 36]}

class Caballo:

    def apostar_caballo(self, dinero_disponible, numero_ganador):
        print(caballos.keys())
        numero_caballo = Ruleta.obtener_opcion_valida('Elige un caballo para apostar: ', list(caballos.keys()))
        dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

        dinero_ganado = 0
        dinero_perdido = 0
        if dinero_apostado > dinero_disponible:
            print("No puedes apostar más dinero del que tienes disponible.")
            return dinero_disponible, 0, 0
        else:
            if str(numero_ganador) in numero_caballo:
                dinero_ganado = dinero_apostado * 18
            else:
                dinero_perdido -= dinero_apostado
        
        return dinero_disponible, dinero_ganado, dinero_perdido