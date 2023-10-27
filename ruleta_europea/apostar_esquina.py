from ruleta_opciones import Ruleta

esquinas = {
        1: [1, 2, 4, 5],
        2: [2, 3, 5, 6],
        3: [4, 5, 7, 8],
        4: [5, 6, 8, 9],
        5: [5, 6, 8, 9],
        6: [7, 8, 10, 11],
        7: [8, 9, 11, 12],
        8: [10, 11, 13, 14],
        9: [11, 12, 14, 15],
        10: [13, 14, 16, 17],
        11: [14, 15, 17, 18],
        12: [16, 17, 19, 20],
        13: [17, 18, 20, 21],
        14: [19, 20, 22, 23],
        15: [20, 21, 23, 24],
        16: [21, 22, 24, 25],
        17: [22, 23, 25, 26],
        18: [23, 24, 26, 27],
        19: [24, 25, 27, 28],
        20: [25, 26, 28, 29],
        21: [26, 27, 29, 30],
        22: [27, 28, 30, 31],
        23: [28, 29, 31, 32],
        24: [29, 30, 32, 33],
        25: [30, 31, 33, 34],
        26: [31, 32, 34, 35],
        27: [32, 33, 35, 36]
    }
class Esquina:


    def obtener_esquinas(self, numero_esquina):
        return esquinas.get(numero_esquina, [])

    def apostar_esquina(self, dinero_disponible, numero_ganador):
        numero_esquina = Ruleta.obtener_opcion_valida('Elige una esquina para apostar (1-27): ', list(esquinas.keys()))
        dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

        esquina_seleccionada = self.obtener_esquinas(numero_esquina)

        dinero_ganado = 0
        dinero_perdido = 0
        if dinero_apostado > dinero_disponible:
            print("No puedes apostar más dinero del que tienes disponible.")
            return dinero_disponible, 0, 0
        else:
            if numero_ganador in esquina_seleccionada:
                dinero_ganado = dinero_apostado * 9
            else:
                dinero_perdido -= dinero_apostado

        return dinero_disponible, dinero_ganado, dinero_perdido
