#       >>  TAREA 3  <<
#   > imports
from lista import *
#   > ej

A = lista(1, lista(1, lista(1, lista(2, lista(3, lista(2, lista(5, listaVacia)))))))
B = lista(9, lista(32, lista(2, lista(1, lista(32, lista(9, lista(13, listaVacia)))))))
#   > funciones abstractas

# mapa: (X -> Y) lista(X) -> lista(Y)
# Devuelve una lista con funcion f aplicada a todos los valores de unaLista.
def mapa(f, unaLista):
    if vacia(unaLista):
        return listaVacia
    else:
        return lista(f(cabeza(unaLista)), mapa(f, cola(unaLista)))


# filtro: (X -> bool) lista(X) -> lista(X)
# Devuelve una lista con todos los valores de unaLista
# donde la funcion operador devuelve True.
def filtro(operador, unaLista):
    if vacia(unaLista):
        return listaVacia
    else:
        if operador(cabeza(unaLista)):
            return lista(cabeza(unaLista), filtro(operador, cola(unaLista)))
        else:
            return filtro(operador, cola(unaLista))


# fold: (X X -> X) X lista(X) -> X
# Procesa los valores de unaLista con la funcion f y devuelve un unico valor
# el valor init se usa como valor inicial para procesar el primer valor
# de la lista y como acumulador para los resultados parciales
# pre-condicion: la lista debe tener al menos un valor.
def fold(f, init, unaLista):
    assert not vacia(unaLista)
    if vacia(cola(unaLista)): # un solo valor
        return f(init, cabeza(unaLista))
    else:
        return fold(f, f(init, cabeza(unaLista)), cola(unaLista))

#   > funciones auxiliares


# juntar: lista(any) lista(any) -> lista(any)
# dadas dos listas, la uncion retorna la
# concatenacion de ambas listas en una.
# ej: juntar(A,B) debe retornar lista(1, lista(1, lista(1, lista(2, lista(3, lista(2, lista(5, lista(9, lista(32, lista(2, lista(1, lista(32, lista(9, lista(13, listaVacia))))))))))))))
def juntar(L1, L2):
    if L1 == None:
        return L2
    return lista(cabeza(L1), juntar(cola(L1), L2))

# Tests:
assert juntar(A,B) == lista(1, lista(1, lista(1, lista(2, lista(3, lista(2, lista(5, lista(9, lista(32, lista(2, lista(1, lista(32, lista(9, lista(13, listaVacia))))))))))))))
assert juntar(A, None) == A
assert juntar(None, B) == B


# pythonListToList: lista -> list
# recibe una lista de python y devuelve una
# lista recursiva.
# ej: listToPythonList([1, 3, 14]) debe retornar lista(1, lista(3, lista(14, listaVacia)))
def pythonListToList(L, miLista = listaVacia):
    if L == []:
        return miLista
    else:
        miLista = lista(L[len(L)-1],miLista)
        return pythonListToList(L[:len(L)-1], miLista)
        
# Tests
assert pythonListToList([1, 3, 14]) == lista(1, lista(3, lista(14, listaVacia)))
assert pythonListToList(['hola', 'como', 'estas', '?']) == lista('hola', lista('como', lista('estas', lista('?', listaVacia))))


# largo: lista(any) -> int
# Devuelve el largo de una lista recursiva.
# ej: largo(lista(1,lista(2,lista(3,lista(4,lista(5,listaVacia)))))) debe retornar 5
def largo(L,length = 0):
    if L == listaVacia:
        return length
    else:
        return largo(cola(L),length = length + 1)

# Tests
assert largo(lista(1,lista(2,lista(3,lista(4,lista(5,listaVacia)))))) == 5
assert largo(A) == 7
assert largo(B) == 7


# mayorNum: num num -> num
# Dados 2 numeros, retorna al mayor
# de ellos.
# ej: mayorNum(5,13) debe retornar 13
def mayorNum(x,y):
    if x > y:
        return x
    else: return y

# Tests
assert mayorNum(5,13) == 13
assert mayorNum(-40,3) == 3


# contar: lista(num) num -> int
# Dados una lista y un num, retorna la
# frecuencia del numero en la lista.
# ej: contar(A,1) debe retornar 3
def contar(L,num):
    listaNum = filtro(lambda x: x==num, L)
    return largo(listaNum)

# Tests
assert contar(A,1) == 3
assert contar(A,2) == 2


# listaRepetitiva: num int -> lista
# Dados un numero x y un entero n, retorna
# una lista con x repetido n veces.
# ej: listaRepetitiva(5,3) debe retornar lista(5, lista(5, lista(5, listaVacia)))
def listaRepetitiva(num, rep, laLista= listaVacia):
    if rep == 1:
        return lista(num, laLista)
    return listaRepetitiva(num,rep-1, lista(num,laLista))

# Tests
assert listaRepetitiva(5,3) == lista(5, lista(5, lista(5, listaVacia)))
assert listaRepetitiva(3.8,1) == lista(3.8, listaVacia)


# rango: int -> lista
# Dado un entero N (N>=1), retorna una lista con
# todos los numeros (en orden creciente) desde
# 1 a N.
# ej: rango(3) debe retornar lista(1, lista(2, lista(3, listaVacia)))
def rango(nums, laLista= listaVacia):
    if nums == 1:
        return lista(1, laLista)
    elif nums > 1:
        return rango(nums-1, lista(nums,laLista))

# Tests
assert rango(3) == lista(1, lista(2, lista(3, listaVacia)))
assert rango(1) == lista(1, listaVacia)


# indice: int lista(any) -> any
# Retorna el valor que se encuentre en el
# lugar i-esimo de la lista. En el caso en
# que i > largo de L, retorna error.
# ej: indice(4,A) debe retornar 2
def indice(i,L):
    assert i <= largo(L)
    if i == 1:
        return cabeza(L)
    else:
        return indice(i-1, cola(L))

# Tests
assert indice(1,A) == 1
assert indice(4,A) == 2
assert indice(2,B) == 32
assert indice(7,B) == 13


# buscar: num lista(num) -> int
# Busca el primer x dentro de la lista y
# retorna el indice en el que se encuentra.
# En caso de no encontrarlo, retorna 0.
# ej: buscar(32,B) debe retornar 2
def buscar(x,L,i=1):
    if L == listaVacia:
        return 0
    if cabeza(L) == x:
        return i
    else:
        return buscar(x,cola(L),i+1)

# Tests
assert buscar(32,B) == 2
assert buscar(22,A) == 0
assert buscar(3,A) == 5


# primerMayorTo0: lista(int) -> int
# Dada un lista, la funcion encuentra el
# primer mayor numero en esta y retorna una
# lista exactamente igual salvo que donde
# estaba ese "primer mayor" ahora hay un 0.
# ej: primerMayorTo0(A) debe retornar lista(1, lista(1, lista(1, lista(2, lista(3, lista(2, lista(0, listaVacia)))))))
def primerMayorTo0(L):
    mayor = fold(mayorNum, 0, L)
    if cabeza(L) == mayor:
        return lista(0, cola(L))
    return lista(cabeza(L), primerMayorTo0(cola(L)))

# Tests
assert primerMayorTo0(A) == lista(1, lista(1, lista(1, lista(2, lista(3, lista(2, lista(0, listaVacia)))))))
assert primerMayorTo0(B) == lista(9, lista(0, lista(2, lista(1, lista(32, lista(9, lista(13, listaVacia)))))))


################################################
#   > funciones


archivo = open('entrada_tarea3.txt','r')
txt1 = archivo.read()
archivo.close()
txt2 = txt1.split('\n')
E = []
for x in txt2:
	E.append(x[x.index('[')+1:len(x)-1])
txt3 = ','.join(E)
txt4 = txt3.split(',')
listaNumerosStr = pythonListToList(txt4)

numeros = mapa(lambda x: int(x), listaNumerosStr)




# < 1 >

# creciente: lista(num) -> lista(num)
# Retorna una lista ordenada en orden creciente
# ej: creciente(lista(3,lista(4,lista(1,lista(2, listaVacia))))) debe retornar lista(1,lista(2,lista(3,lista(4, listaVacia))))
def creciente(L, new = listaVacia):
    if L == listaVacia:
        return new
    mayor = fold(mayorNum, 0, L)
    rep = contar(L, mayor)
    filtrada = filtro(lambda x: x!= mayor, L)
    return creciente(filtrada, juntar(lista(mayor, listaVacia), new))
    # return creciente(filtrada, juntar(listaRepetitiva(mayor,rep), new))       <- suprimida porque retornaba con repetidos.

# Tests
assert creciente(A) == pythonListToList([1,2,3,5])
assert creciente(B) == pythonListToList([1,2,9,13,32])


# < 2 >

# salenMasDeUnaVez: lista(int) -> lista(int)
# Retorna una lista con todos los números de
# la lista con frecuencia mayor a 1.
# ej: salenMasDeUnaVez(A) debe retornar lista(1, lista(2, listaVacia))
def salenMasDeUnaVez(L):
    mayor = fold(mayorNum, 0, L)
    rango_ = rango(mayor)
    return filtro(lambda x: contar(L, x) > 1, rango_)

# Tests
assert salenMasDeUnaVez(A) == lista(1, lista(2, listaVacia))
assert salenMasDeUnaVez(B) == lista(9, lista(32, listaVacia))



# < 3 >

# noSorteados: lista(int) -> lista(int)
# Retorna un lista con todos los números en el
# rango [1, 41] que nunca salieron en la lista.
# ej: noSorteados(B) debe retornar pythonListToList([3,4,5,6,7,8,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41])
def noSorteados(L):
    # mayor = fold(mayorNum, 0, L)                                              <- suprimida para que funcione solo con meyor = 41.
    mayor = 41
    rango_ = rango(mayor)
    return filtro(lambda x: contar(L, x)==0, rango_)

# Tests
assert noSorteados(numeros) == lista(11, lista(12, lista(13, lista(16, lista(17, lista(19, lista(20, lista(27, lista(30, lista(32, lista(40, listaVacia)))))))))))
assert noSorteados(A) == pythonListToList([4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41])
assert noSorteados(B) == pythonListToList([3,4,5,6,7,8,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41])


# < 4 >

# los4MasSorteados: lista -> lista
# Retorna una lista con los 4 numeros con mas frecuencia
# (en caso en que haya numeros con misma frecuencia, se
# considera primero el menor).
# ej: los4MasSorteados(numeros) debe retornar lista(9, lista(23, lista(41, lista(8, listaVacia))))
def los4MasSorteados(L):
    mayor = fold(mayorNum, 0, L)
    rango_ = rango(mayor)

    # 1er mas sorteado
    frecList = mapa(lambda x: contar(L, x), rango_)
    mayorFrec = fold(mayorNum, 0, frecList)
    i1 = buscar(mayorFrec, frecList)
    n1 = indice(i1, rango_)

    # 2o mas sorteado
    frecList2 = primerMayorTo0(frecList)
    mayorFrec2 = fold(mayorNum, 0, frecList2)
    i2 = buscar(mayorFrec2, frecList2)
    n2 = indice(i2, rango_)

    # 3o mas sorteado
    frecList3 = primerMayorTo0(frecList2)
    mayorFrec3 = fold(mayorNum, 0, frecList3)
    i3 = buscar(mayorFrec3, frecList3)
    n3 = indice(i3, rango_)

    # 4o mas sorteado
    frecList4 = primerMayorTo0(frecList3)
    mayorFrec4 = fold(mayorNum, 0, frecList4)
    i4 = buscar(mayorFrec4, frecList4)
    n4 = indice(i4, rango_)
    
    return lista(n1, lista(n2, lista(n3, lista(n4, listaVacia))))
    
# Tests
assert los4MasSorteados(numeros) == lista(9, lista(23, lista(41, lista(8, listaVacia))))
assert los4MasSorteados(A) == lista(1, lista(2, lista(3, lista(5, listaVacia))))
assert los4MasSorteados(B) == lista(9, lista(32, lista(1, lista(2, listaVacia))))

