from ruleta_opciones import Ruleta

class DocenaColumna:

    def apostar_docena(dinero_disponible, numero_ganador):
        docena_elegida = Ruleta.obtener_opcion_valida('Elige la docena a la que quieres apostar (1, 2 o 3): ', [1, 2, 3])
        dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

        dinero_ganado = 0

        if (docena_elegida == 1 and numero_ganador in range(1, 13)) or \
        (docena_elegida == 2 and numero_ganador in range(13, 25)) or \
        (docena_elegida == 3 and numero_ganador in range(25, 37)):
            dinero_ganado = dinero_apostado * 3
            dinero_disponible += dinero_ganado
        else:
            dinero_disponible -= dinero_apostado

        return dinero_disponible, dinero_ganado, dinero_apostado

    def obtener_columna(self, numero_columna):
        columnas = {
            1: [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
            2: [2, 5, 8, 11, 14, 17, 20, 13, 26, 29, 32, 35],
            3: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
        }
        return columnas.get(numero_columna, [])

    def apostar_columna(self, dinero_disponible, numero_ganador):
        numero_columna = Ruleta.obtener_opcion_valida('Elige una columna para apostar (1-3): ', [1, 2, 3])
        dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

        columna_seleccionada = self.obtener_columna(numero_columna)

        dinero_ganado = 0

        if numero_ganador in columna_seleccionada:
            dinero_ganado = dinero_apostado * 3
            dinero_disponible += dinero_ganado
        else:
            dinero_disponible -= dinero_apostado

        return dinero_disponible, dinero_ganado, dinero_apostado

    def obtener_doble_columna(self, numero_doble_columna):
        columnas = {
            1: [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
            2: [2, 5, 8, 11, 14, 17, 20, 13, 26, 29, 32, 35],
            3: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
        }
        
        doble_columna = {}
        for columna, numeros in columnas.items():
            siguiente_columna = columna + 1 if columna < 3 else 1
            doble_columna[columna] = numeros + columnas[siguiente_columna]
        
        return doble_columna.get(numero_doble_columna, [])

    def apostar_doble_columa(self, dinero_disponible, numero_ganador):
        numero_doble_columna = Ruleta.obtener_opcion_valida('Elige la doble columna para apostar (1, 2, 3): ', [1, 2, 3])
        dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

        doble_columna_seleccionada = self.obtener_doble_columna(numero_doble_columna)

        dinero_ganado = 0

        if numero_ganador in doble_columna_seleccionada:
            dinero_ganado = dinero_apostado * 1.5
            dinero_disponible += dinero_ganado
        else:
            dinero_disponible -= dinero_apostado
        
        return dinero_disponible, dinero_ganado, dinero_apostado

    def apostar_doble_docena(dinero_disponible, numero_ganador):
        doble_docena_elegida = Ruleta.obtener_opcion_valida('Elige la doble docena a la que quieres apostar (1, 2, 3): ', [1, 2, 3])
        dinero_apostado = int(input('Ingrese la cantidad a apostar: ')) 

        dinero_ganado = 0

        if (doble_docena_elegida == 1 and numero_ganador in range(1, 25)) or \
        (doble_docena_elegida == 2 and numero_ganador in range(13, 37)) or \
        (doble_docena_elegida == 3 and (numero_ganador in range(25, 37) or numero_ganador in range(1, 13))):
            dinero_ganado = dinero_apostado * 1.5
            dinero_disponible += dinero_ganado
        else:
            dinero_disponible -= dinero_apostado
        
        return dinero_disponible, dinero_ganado, dinero_apostado   