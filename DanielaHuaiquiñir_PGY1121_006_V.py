detalle_lotes = [
    {'Número': 'Lote 1', 'Tamaño': '700 m²', 'Precio': '$25.000.000'},
    {'Número': 'Lote 2', 'Tamaño': '600 m²', 'Precio': '$20.000.000'},
    {'Número': 'Lote 3', 'Tamaño': '500 m²', 'Precio': '$15.000.000'},
    {'Número': 'Lote 4', 'Tamaño': '400 m²', 'Precio': '$10.000.000'},
]

'''Genera 4 filas de izquierda a derecha y 4 columnas de arriba hacia abajo,
quedando en forma de un cuadrado 4X4 = 16 espacios libres (inicialmente).'''
lotes_mapa = [[' ' for _ in range(4)] for _ in range(4)]

lotes_seleccionados = [] #Lista (inicialmente vacía) de lotes que hayan sido seleccionados.
lista_clientes = [] #Lista (inicialmente vacía) de clientes que hayan adquirido lotes.

def ver_lotes():
    print("\nMapa de lotes:")
    for fila in lotes_mapa:
        for disponibilidad in fila:
            #Adición de corchetes [] con o sin marca (varia) a la forma generada para segmentar.
            print('[ ]' if disponibilidad == ' ' else '[X]', end=' ')
        print()

def seleccion_lote():
    while True:
        try:
            select_fila = int(input("\nSelecciona una fila (0-3): "))
            '''0 en realidad sería nuestra 1º fila, mientras 3 nuestra última y 4º fila.
               Esto considera todo los espacios (lotes) ubicados en la esquina superior
               de manera horizontal en la forma generada (cuadrado).'''

            select_columna = int(input("Selecciona una columna (0-3): "))
            '''Sigue la misma condición anterior, salvo que las columnas son todos
               aquellos espacios (lotes) ubicados en forma vertical que son ubicados
               por una coordenada (número ingresado) de la fila seleccionada.'''

            #Comprobación de error en el ingreso de UNO DE LOS DOS datos.
            if select_fila < 0 or select_fila >= 4 or select_columna < 0 or select_columna >= 4:
                print("Las coordenadas ingresadas no son válidas o no existen. \nPor favor, intente nuevamente.")
                continue

            #Comprobación de que el espacio (lote) SE ENCUENTRE VACÍO, por tanto, ESTE DISPONIBLE.
            if lotes_mapa[select_fila][select_columna] == ' ':
                break
            else:
                print("El lote seleccionado ya se encuentra ocupado. \nPor favor, elija y seleccione otro.")

        #Comprobación de error en el ingreso de AMBOS datos.
        except ValueError:
            print("El valor ingresado no es válido. \nPor favor, intente nuevamente.")
            continue

    #Datos del cliente:
    rut = input("\nIngrese el RUT del cliente: ")
    nombres = input("Ingrese el/los nombre(s) del cliente: ")
    apellidos = input("Ingrese el/los apellido(s) del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    email = input("Ingrese el correo electrónico del cliente: ")

    lote_seleccionado = detalle_lotes[select_columna]
    lotes_seleccionados.append({
        'Número': lote_seleccionado['Número'],
        'Tamaño': lote_seleccionado['Tamaño'],
        'Precio': lote_seleccionado['Precio'],
        'Cliente': {
            'RUT': rut,
            'Nombres': nombres,
            'Apellidos': apellidos,
            'Teléfono': telefono,
            'Email': email
        }
    })
    '''Se añaden datos al final de la lista de lotes_seleccionados
       de aquellos lotes que ya fueron seleccionados con éxito.'''

    lotes_mapa[select_fila][select_columna] = 'X'
    '''Una vez seleccionado el lote, se deja una marca en este para
       indicar que este ha sido ocupado y/o no se encuentra disponible.'''

    #Mensaje de éxito de operación de selección:
    print("_______________________________________________")
    print("El lote seleccionado ha sido ocupado con éxito.")

def mostrar_detalles():
    if len(lotes_seleccionados) > 0:
        print("\nDetalles de lotes adquiridos:") #Indica los datos del dueño(a), número de lote, tamaño y precio de este
        for lote in lotes_seleccionados:
            print("Número:", lote['Número'])
            print("Tamaño:", lote['Tamaño'])
            print("Precio:", lote['Precio'])
            print("Cliente:")
            cliente = lote['Cliente']
            print("\tRUT:", cliente['RUT'])
            print("\tNombres:", cliente['Nombres'])
            print("\tTeléfono:", cliente['Teléfono'])
            print("\tEmail:", cliente['Email'])
            print()
    else:
        print("No hay lotes seleccionados por el momento.") #Mensaje para cuando lista de lotes seleccionados SE ENCUENTRE VACÍA.

def mostrar_clientes():
    if len(lotes_seleccionados) > 0: #Comprobación para verificar que la lista de clientes NO SE ENCUENTRE VACÍA.
        print("\nClientes que han comprado un lote:")
        for lote in lotes_seleccionados:
            cliente = lote['Cliente']
            print("RUT:", cliente['RUT'])
            print("Nombres:", cliente['Nombres'])
            print("Teléfono:", cliente['Teléfono'])
            print("Email:", cliente['Email'])
            print()
    else:
        print("No hay clientes registrados por el momento.") #Mensaje para cuando lista de clientes SE ENCUENTRE VACÍA.

def menu_principal():
    while True:
        print("\n---------------- LOTES DUOC ----------------")
        print("---1. Ver disponibilidad de lotes-----------")
        print("---2. Seleccionar un lote-------------------")
        print("---3. Ver detalles del lote seleccionado----")
        print("---4. Ver clientes--------------------------")
        print("---5. Salir---------------------------------")

        try:
            opcion = int(input("\nIngrese una opción: "))
        except ValueError:
            print("La opción ingresada no es válida. \nPor favor, intente nuevamente.")
            continue


        if opcion == 1:
            ver_lotes() #Muestra mapa de lotes completo.
        elif opcion == 2:
            seleccion_lote() #Proceso de selección de lote.
        elif opcion == 3:
            mostrar_detalles() #Listado de lotes que ya han sido seleccionados.
        elif opcion == 4:
            mostrar_clientes() #Listado de clientes ya asociados.
        elif opcion == 5:
            print("Gracias por usar el sistema de Loteos Duoc. \n¡Hasta pronto!")
            print("Has salido de la aplicación.") #Mensaje despedida (Termino de ejecución).
            break
        else:
            print("La opción ingresada no es válida. \nPor favor, intente nuevamente.")

#Ejecución de menú de inicio y opciones.
menu_principal()