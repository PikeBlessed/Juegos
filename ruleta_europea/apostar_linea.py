from ruleta_opciones import Ruleta


lineas = {
    1: [0, 1, 2],
    2: [0, 2, 3],
    3: [1, 2, 3],
    4: [4, 5, 6],
    5: [7, 8, 9],
    6: [10, 11, 12],
    7: [13, 14, 15],
    8: [16, 17, 18],
    9: [19, 20, 21],
    10: [22, 23, 24],
    11: [25, 26, 27],
    12: [28, 29, 30],
    13: [31, 32, 33],
    14: [34, 35, 36]
}
class Linea:
    def obtener_linea(self, numero_linea):
        return lineas.get(numero_linea, [])

    def apostar_linea(self, dinero_disponible, numero_ganador):
        numero_linea = Ruleta.obtener_opcion_valida('Elige una linea para apostar (1-14): ', list(lineas.keys()))
        dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

        linea_seleccionada = self.obtener_linea(numero_linea)

        dinero_ganado = 0
        dinero_perdido = 0
        if dinero_apostado > dinero_disponible:
            print("No puedes apostar más dinero del que tienes disponible.")
            return dinero_disponible, 0, 0
        else:
            if numero_ganador in linea_seleccionada:
                dinero_ganado = dinero_apostado * 12
            else:
                dinero_perdido -= dinero_apostado

        return dinero_disponible, dinero_ganado, dinero_perdido
