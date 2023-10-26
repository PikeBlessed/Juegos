from ruleta_opciones import Ruleta
from apostar_caballo import Caballo
from apostar_docena_columna import DocenaColumna
from apostar_esquina import Esquina
from apostar_seisena import Seisena
from apostar_pleno import Pleno
from apostar_linea import Linea
from apostar_48 import CuarentaPorciento

print('Bienvenido a la ruleta de OctaDP')
dinero_disponible = 1000
while dinero_disponible > 0:
    print(f'Su dinero disponible es: {dinero_disponible}')
    apostar = Ruleta.obtener_opcion_valida('Le gustaria apostar (s/n): ', ['s', 'n'])

    if apostar == 's':
        opciones_elegidas = []
        while True:
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
            print('0. Girar ruleta')
            print('-' * 20)

            opcion = input('Ingrese la opcion deseada: ')
            print('-' * 20)
            if opcion.isdigit():
                opcion = int(opcion)
                if opcion == 0:
                    break  # Salir del bucle interno y girar la ruleta
                elif 0 < opcion <= 12:
                    opciones_elegidas.append(opcion)
                else:
                    print('Por favor, elija una opción válida.')
                    print('-' * 20)
            else:
                print('Por favor, elija una opción válida.')
                print('-' * 20)

        docena_columna = DocenaColumna()
        esquina = Esquina()
        caballo = Caballo()
        linea = Linea()

        numero_ganador = Ruleta.girar_ruleta()
        dinero_ganado_total = 0
        dinero_perdido = 0
        for opcion in opciones_elegidas:
            if opcion == 1:
                dinero_disponible, dinero_ganado, dinero_apostado = CuarentaPorciento.apostar_par_impar(dinero_disponible, numero_ganador)
            elif opcion == 2:
                dinero_disponible, dinero_ganado, dinero_apostado = CuarentaPorciento.apostar_color(dinero_disponible, numero_ganador)
            elif opcion == 3:
                dinero_disponible, dinero_ganado, dinero_apostado = CuarentaPorciento.apostar_falta_pasa(dinero_disponible, numero_ganador)
            elif opcion == 4:
                dinero_disponible, dinero_ganado, dinero_apostado = DocenaColumna.apostar_docena(dinero_disponible, numero_ganador)
            elif opcion == 5:
                dinero_disponible, dinero_ganado, dinero_apostado = docena_columna.apostar_columna(dinero_disponible, numero_ganador)
            elif opcion == 6:
                dinero_disponible, dinero_ganado, dinero_apostado = docena_columna.apostar_doble_columa(dinero_disponible, numero_ganador)
            elif opcion == 7:
                dinero_disponible, dinero_ganado, dinero_apostado = DocenaColumna.apostar_doble_docena(dinero_disponible, numero_ganador)
            elif opcion == 8:
                dinero_disponible, dinero_ganado, dinero_apostado = Seisena.apostar_seisena(dinero_disponible, numero_ganador)
            elif opcion == 9:
                dinero_disponible, dinero_ganado, dinero_apostado = esquina.apostar_esquina(dinero_disponible, numero_ganador)
            elif opcion == 10:
                dinero_disponible, dinero_ganado, dinero_apostado = linea.apostar_linea(dinero_disponible, numero_ganador)
            elif opcion == 11:
                dinero_disponible, dinero_ganado, dinero_apostado = caballo.apostar_caballo(dinero_disponible, numero_ganador)
            elif opcion == 12:
                dinero_disponible, dinero_ganado, dinero_apostado = Pleno.apostar_numero(dinero_disponible, numero_ganador)
            else:
                print('Por favor elija una opcion correcta')
            dinero_perdido -= dinero_apostado
            dinero_ganado_total += dinero_ganado
            
        print('-' * 20)
        print(f'El numero ganador es: {numero_ganador}')
        print(f'Dinero total ganado en esta apuesta: {dinero_ganado_total}')
        print(f'Dinero total perdido en esta apuesta: {dinero_perdido}')
        dinero_disponible += dinero_ganado_total
        print(f'Dinero disponible: {dinero_disponible}')
        print('-' * 20)
    else:
        print('Muchas gracias por jugar, esperamos verlo pronto')
        break
