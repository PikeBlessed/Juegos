import random

def crear_opcion(numero_ganador):
    if numero_ganador == 0:
        return 'verde'
    elif numero_ganador in (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35):
        return 'negro'
    else:
        return 'rojo'
    
def girar_ruleta():
    numero_ganador = random.randint(0, 36)
    return numero_ganador

def obtener_opcion_valida(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje)
        if opcion.isdigit() and int(opcion) in opciones_validas:
            return int(opcion)
        elif opcion in opciones_validas:
            return opcion
        else:
            print('Opcion invalida. Por favor, elige una opcion valida.')

def apostar_color(dinero_disponible, numero_ganador):
    color_elegido = obtener_opcion_valida('Elige el color al que quieres apostar (rojo, negro o verde): ', ['rojo', 'negro', 'verde'])
    dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

    color_ganador = crear_opcion(numero_ganador)

    dinero_ganado = 0
    if color_elegido == color_ganador:
        if color_ganador == 'verde':
            dinero_ganado = dinero_apostado * 36
        else:
            dinero_ganado = dinero_apostado * 2

        dinero_disponible += dinero_ganado
    else:
        dinero_disponible -= dinero_apostado

    return dinero_disponible, dinero_ganado

def apostar_par_impar(dinero_disponible, numero_ganador):
    par_impar_elegido = obtener_opcion_valida('Elige si quieres apostar a un número par o impar: ', ['par', 'impar'])
    dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

    dinero_ganado = 0

    if par_impar_elegido == 'par':
        if numero_ganador % 2 == 0:
            dinero_ganado = dinero_apostado * 2
            dinero_disponible += dinero_ganado
        else:
            dinero_disponible -= dinero_apostado
    elif par_impar_elegido == 'impar':
        if numero_ganador % 2 == 1:
            dinero_ganado = dinero_apostado * 2
            dinero_disponible += dinero_ganado
        else:
            dinero_disponible -= dinero_apostado

    return dinero_disponible, dinero_ganado
         

def apostar_falta_pasa(dinero_disponible, numero_ganador):
    falta_pasa_elegido = obtener_opcion_valida('Elige falta o pasa: ', ['falta', 'pasa'])
    dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

    dinero_ganado = 0

    if falta_pasa_elegido == 'falta':
        if numero_ganador in range(1, 19):
            dinero_ganado = dinero_apostado * 2
            dinero_disponible += dinero_ganado
        else:
            dinero_disponible -= dinero_apostado
    elif falta_pasa_elegido == 'pasa':
        if numero_ganador in range(19, 37):
            dinero_ganado = dinero_apostado * 2
            dinero_disponible += dinero_ganado
        else:
            dinero_disponible -= dinero_apostado

    return dinero_disponible, dinero_ganado


def apostar_docena(dinero_disponible, numero_ganador):
    docena_elegida = obtener_opcion_valida('Elige la docena a la que quieres apostar (1, 2 o 3): ', [1, 2, 3])
    dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

    dinero_ganado = 0

    if (docena_elegida == 1 and numero_ganador in range(1, 13)) or \
    (docena_elegida == 2 and numero_ganador in range(13, 25)) or \
    (docena_elegida == 3 and numero_ganador in range(25, 37)):
        dinero_ganado = dinero_apostado * 3
        dinero_disponible += dinero_ganado
    else:
        dinero_disponible -= dinero_apostado

    return dinero_disponible, dinero_ganado

def obtener_columna(numero_columna):
    columnas = {
        1: [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
        2: [2, 5, 8, 11, 14, 17, 20, 13, 26, 29, 32, 35],
        3: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    }
    return columnas.get(numero_columna, [])

def apostar_columna(dinero_disponible, numero_ganador):
    numero_columna = obtener_opcion_valida('Elige una columna para apostar (1-3): ', [1, 2, 3])
    dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

    columna_seleccionada = obtener_columna(numero_columna)

    dinero_ganado = 0

    if numero_ganador in columna_seleccionada:
        dinero_ganado = dinero_apostado * 3
        dinero_disponible += dinero_ganado
    else:
        dinero_disponible -= dinero_apostado

    return dinero_disponible, dinero_ganado

def obtener_doble_columna(numero_doble_columna):
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

def apostar_doble_columa(dinero_disponible, numero_ganador):
    numero_doble_columna = obtener_opcion_valida('Elige la doble columna para apostar (1, 2, 3): ', [1, 2, 3])
    dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

    doble_columna_seleccionada = obtener_doble_columna(numero_doble_columna)

    dinero_ganado = 0

    if numero_ganador in doble_columna_seleccionada:
        dinero_ganado = dinero_apostado * 1.5
        dinero_disponible += dinero_ganado
    else:
        dinero_disponible -= dinero_apostado
    
    return dinero_disponible, dinero_ganado

def apostar_doble_docena(dinero_disponible, numero_ganador):
    doble_docena_elegida = obtener_opcion_valida('Elige la doble docena a la que quieres apostar (1, 2, 3): ', [1, 2, 3])
    dinero_apostado = int(input('Ingrese la cantidad a apostar: ')) 

    dinero_ganado = 0

    if (doble_docena_elegida == 1 and numero_ganador in range(1, 25)) or \
    (doble_docena_elegida == 2 and numero_ganador in range(13, 37)) or \
    (doble_docena_elegida == 3 and (numero_ganador in range(25, 37) or numero_ganador in range(1, 13))):
        dinero_ganado = dinero_apostado * 1.5
        dinero_disponible += dinero_ganado
    else:
        dinero_disponible -= dinero_apostado
    
    return dinero_disponible, dinero_ganado

def apostar_seisena(dinero_disponible, numero_ganador):
    seisena_elegida = obtener_opcion_valida('Elige la seisena a la que desea apostar (1, 2, 3, 4, 5, 6): ', [1, 2, 3, 4, 5, 6])
    dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

    dinero_ganado = 0

    if (seisena_elegida == 1 and numero_ganador in range(1, 7)) or \
    (seisena_elegida == 2 and numero_ganador in range(7, 13)) or \
    (seisena_elegida == 3 and numero_ganador in range(13, 19)) or \
    (seisena_elegida == 4 and numero_ganador in range(19, 25)) or \
    (seisena_elegida == 5 and numero_ganador in range(25, 31)) or \
    (seisena_elegida == 6 and numero_ganador in range(31, 37)):
        dinero_ganado = dinero_apostado * 6
        dinero_disponible += dinero_ganado
    else:
        dinero_disponible -= dinero_apostado

    return dinero_disponible, dinero_ganado

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

def obtener_esquinas(numero_esquina):
    return esquinas.get(numero_esquina, [])

def apostar_esquina(dinero_disponible, numero_ganador):
    numero_esquina = obtener_opcion_valida('Elige una esquina para apostar (1-27): ', list(esquinas.keys()))
    dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

    esquina_seleccionada = obtener_esquinas(numero_esquina)

    dinero_ganado = 0

    if numero_ganador in esquina_seleccionada:
        dinero_ganado = dinero_apostado * 9
        dinero_disponible += dinero_ganado
    else:
        dinero_disponible -= dinero_apostado

    return dinero_disponible, dinero_ganado

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

def obtener_linea(numero_linea):
    return lineas.get(numero_linea, [])

def apostar_linea(dinero_disponible, numero_ganador):
    numero_linea = obtener_opcion_valida('Elige una linea para apostar (1-14): ', list(lineas.keys()))
    dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

    linea_seleccionada = obtener_linea(numero_linea)

    dinero_ganado = 0

    if numero_ganador in linea_seleccionada:
        dinero_ganado = dinero_apostado * 12
        dinero_disponible += dinero_ganado
    else:
        dinero_disponible -= dinero_apostado

    return dinero_disponible, dinero_ganado

caballos = {}

def obtener_caballo(numero_caballo):
    for fila in range(1, 13):
        for columna in range(1, 4):
            numero_actual = (fila - 1) * 3 + columna
            if columna < 3:
                # Caballo horizontal (dos números en la misma fila)
                caballos[f'Caballo {numero_actual}-{numero_actual + 1}'] = [numero_actual, numero_actual + 1]
            if fila < 12:
                # Caballo vertical (dos números adyacentes en diferentes filas)
                caballos[f'Caballo {numero_actual}-{numero_actual + 3}'] = [numero_actual, numero_actual + 3]
    return caballos.get(numero_caballo, [])

def apostar_caballo(dinero_disponible, numero_ganador):
    numero_caballo = obtener_opcion_valida('Elige un caballo para apostar: ', list(caballos.keys()))
    dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

    caballo_seleccionado = obtener_caballo(numero_caballo)

    dinero_ganado = 0

    if numero_ganador in caballo_seleccionado:
        dinero_ganado = dinero_apostado * 18
        dinero_disponible += dinero_ganado
    else:
        dinero_disponible -= dinero_apostado
    
    return dinero_disponible, dinero_ganado

numeros = list(range(0, 37))

def apostar_numero(dinero_disponible, numero_ganador):
    numero_elegido = obtener_opcion_valida('Ingrese el número al que desea apostar(0, 36): ', list(numeros))
    dinero_apostado = int(input('Ingrese la cantidad a apostar: '))

    dinero_ganado = 0

    if numero_ganador == numero_elegido:
        dinero_ganado = dinero_apostado * 3612
        dinero_disponible += dinero_ganado
    else:
        dinero_disponible -= dinero_apostado

    return dinero_disponible, dinero_ganado

if __name__ == '__main__':
    print('Bienvenido a la ruleta de OctaDP')
    dinero_disponible = 1000
    while dinero_disponible > 0:
        print('Elige una opción de apuesta:')
        print('1. Apostar en un número par o impar')
        print('2. Apostar en un color')
        print('3. Apostar a falta o pasa')
        print('4. Apostar en una docena')
        print('5. Apostar en una columna')
        print('6. Apostar en una doble columna')
        print('7. Apostar en una doble docena')
        print('8. Apostar en una seisena')
        print('9. Apostar en una esquina de 4')
        print('10. Apostar en una linea de 3')
        print('11. Apostar en un caballo de 2')
        print('12. Apostar en un pleno de 1')
        print('0. Salir')

        opcion = int(input('Ingrese la opcion deseada: '))

        numero_ganador = girar_ruleta()
        dinero_ganado = 0
        if opcion == 0:
            print(f'Gracias por jugar. Tu saldo final es: {dinero_disponible}')
            break
        elif opcion == 1:
            dinero_disponible, dinero_ganado = apostar_par_impar(dinero_disponible, numero_ganador)
        elif opcion == 2:
            dinero_disponible, dinero_ganado = apostar_color(dinero_disponible, numero_ganador)
        elif opcion == 3:
            dinero_disponible, dinero_ganado = apostar_falta_pasa(dinero_disponible, numero_ganador)
        elif opcion == 4:
            dinero_disponible, dinero_ganado = apostar_docena(dinero_disponible, numero_ganador)
        elif opcion == 5:
            dinero_disponible, dinero_ganado = apostar_columna(dinero_disponible, numero_ganador)
        elif opcion == 6:
            dinero_disponible, dinero_ganado = apostar_doble_columa(dinero_disponible, numero_ganador)
        elif opcion == 7:
            dinero_disponible, dinero_ganado = apostar_doble_docena(dinero_disponible, numero_ganador)
        elif opcion == 8:
            dinero_disponible, dinero_ganado = apostar_seisena(dinero_disponible, numero_ganador)
        elif opcion == 9:
            dinero_disponible, dinero_ganado = apostar_esquina(dinero_disponible, numero_ganador)
        elif opcion == 10:
            dinero_disponible, dinero_ganado = apostar_linea(dinero_disponible, numero_ganador)
        elif opcion == 11:
            dinero_disponible, dinero_ganado = apostar_caballo(dinero_disponible, numero_ganador)
        elif opcion == 12:
            dinero_disponible, dinero_ganado = apostar_numero(dinero_disponible, numero_ganador)
        else:
            print('Por favor elija una opcion correcta')
        print('-' * 20)
        print(f'El numero ganador es: {numero_ganador}')
        print(f'Dinero ganado en esta apuesta: {dinero_ganado}')
        print(f'Dinero disponible: {dinero_disponible}')
        print('-' * 20)



