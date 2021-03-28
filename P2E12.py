#La idea es tratar de programar una de las partes principales del juego “Buscaminas”. La idea
#es que dado una estructura que dice que celdas tienen minas y que celdas no las tienen, como
#la siguiente:
minas = [
'-*-*-',
'--*--',
'----*',
'*----',
]

#Generar otra que indique en las celdas vacías la cantidad de bombas que la rodean, para el ejemplo
#anterior, sería:
#[
#'1*3*1',
#'12*32',
#'1212*',
#'*1011',
#]

def procesar_minas(lista_minas):
    """procesar_minas toma una lista de Strings, la procesa y devuelve otra lista de Strings procesada."""
    resultado = list()
    for f in range(len(lista_minas)):
        resultado.append(procesar_fila(f, lista_minas))
    return resultado

def procesar_fila(index_fila, lista_minas):
    """procesar_fila recibe como parametro una lista de Strings y un indice dentro del rango de la lista, los procesa y devuelve una cadena de caracteres."""
    fila = ''
    for c in range(len(lista_minas[index_fila])):
        fila = fila + procesar_caracter(lista_minas, index_fila, c)
    return fila

def procesar_caracter(lista_minas, index_fila, index_caracter):
    """procesar_caracter recibe una lista de Strings y dos indices, uno dentro del rango de la lista y otro dentro del rango de la cadena de caracteres.
    devuelve un caracter numerico en base a la cantidad de caracteres vecinos que contengan un asterisco o retorna un asterisco en caso de ser el mismo ese simbolo. """
    if lista_minas[index_fila][index_caracter] == '*':
        return '*'
    else:
        cont = 0
        for x in range(3):
            for y in range(3):
#El siguiente "if" podria escribirse en un solo renglon, los dejo anidados por legibilidad
                if index_fila+x-1 >= 0 and index_fila+x-1 < len(lista_minas):
                    if index_caracter+y-1 >= 0 and index_caracter++y-1 < len(lista_minas[index_fila]):
                        if lista_minas[index_fila+x-1][index_caracter+y-1] == '*':
                            cont+=1
        return str(cont)

resul = procesar_minas(minas)
for elem in resul:
    print(elem)
input("pesione ENTER para salir")
