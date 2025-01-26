import numpy as np

def estadoEstable(matrizT):
    n = 2
    while (np.any(matrizT != matrizT[0])): 
        matrizT = np.linalg.matrix_power(matrizT, n)
        matrizT = np.round(matrizT, 3)
        print(matrizT)
        n += 1
    return matrizT

empresa = input("Escriba el nombre de su empresa: ")

valorVariables = int(input(f"¿Cuántos niveles de maestría tienen en {empresa}?: "))

n = valorVariables
matriz = np.zeros((n, n))

lista = list()
print("Ponga el nombre a cada nivel")
for i in range(n):
    nivel = input(f"Nombre del nivel {i+1}: ")
    lista.append(nivel)

def valorFilas(vector):
    for v in vector:
        if v != 1.0:
            return False
    return True

def politicas(matrizT, lista, nPolitica):
    vC = False
    contador = 0
    valor0 = 2
    while ((valor0 > 1 or valor0 < 0) or (valor1 > 1 or valor1 < 0) or (valor2 > 1 or valor2 < 0) or not vC):
        if (contador >= 1):
            print("Debe volver a llenar la matriz, no se aceptan valores mayores que 1 o negativos.")
            print(matrizT)
            print(matrizT.sum(1))
            print(f"Todas las filas suman un valor de 1: {vC}")
            print("Si la suma de los valores de alguna fila no es igual a 1, vuelva a rellenar los campos de tal manera que ello se cumpla.\n")

        contador += 1

        for j in lista:
            for k in lista:
                if (j == lista[-1]):
                    if (j != lista[-1] or (k != lista[0] and k != lista[-1])):
                        pass
                    elif (nPolitica == 2):
                        i0 = lista.index(j) - 1
                        valor0 = float(input(f"Probabilidad de {j} a {lista[i0]}, si llega a renunciar: "))
                        valor1 = float(input(f"Probabilidad de {j} a {j}: "))
                        matrizT[lista.index(j)][i0] = valor0
                        matrizT[lista.index(j)][lista.index(j)] = valor1
                        break
                    else: 
                        valor0 = float(input(f"Probabilidad de {j} a {k}: "))
                        matrizT[lista.index(j)][lista.index(k)] = valor0
                elif (j == lista[0]):
                    valor0 = 0
                    if (k == lista[1]):
                        valor0 = float(input(f"Probabilidad de {j} a {k}: "))
                    elif (k == lista[0]):
                        valor0 = float(input(f"Probabilidad de mantenerse como {j} o renunciar: "))
                    matrizT[lista.index(j)][lista.index(k)] = valor0
                else:
                    if (nPolitica == 1):
                        i2 = lista.index(j) + 1
                        valor0 = float(input(f"Probabilidad de {j} a {lista[0]}: "))
                        valor1 = float(input(f"Probabilidad de {j} a {j}: "))
                        valor2 = float(input(f"Probabilidad de {j} a {lista[i2]}: "))
                        matrizT[lista.index(j)][lista.index(j)] = valor1
                        matrizT[lista.index(j)][0] = valor0
                        matrizT[lista.index(j)][i2] = valor2
                        break
                    elif (nPolitica == 2):
                        i0 = lista.index(j) - 1
                        i2 = lista.index(j) + 1
                        valor0 = float(input(f"Probabilidad de {j} a {lista[i0]}: "))
                        valor1 = float(input(f"Probabilidad de {j} a {j}: "))
                        valor2 = float(input(f"Probabilidad de {j} a {lista[i2]}: "))
                        matrizT[lista.index(j)][lista.index(j)] = valor1
                        matrizT[lista.index(j)][0] = valor0
                        matrizT[lista.index(j)][i2] = valor2
                        break
                        
        vC = valorFilas(matrizT.sum(1))
    return matrizT

print( "\033[1m" + "\nLlene los datos para comprender la política #1" + "\033[0;0m")
matrizP1 = politicas(matriz, lista, 1)

matriz = np.zeros((n,n))

print( "\033[1m" + "\nLlene los datos para comprender la política #2" + "\033[0;0m")
matrizP2 = politicas(matriz, lista, 2)

print("La matriz inicial de la política #1: ")
print(matrizP1)

print("La matriz inicial de la política #2: ")
print(matrizP2)

def es_matriz_estable(P):

    def filas_suman_uno(P):
        return np.allclose(np.sum(P, axis=1), 1)

    def es_irreducible(P):
        n = P.shape[0]
        alcanzabilidad = np.linalg.matrix_power(P, n - 1) > 0
        return np.all(np.sum(alcanzabilidad, axis=1) > 0)

    def es_aperiodica(P):
        n = P.shape[0]
        alcanzabilidad = np.linalg.matrix_power(P, n - 1) > 0
        periodos = []
        for i in range(n):
            for j in range(n):
                if alcanzabilidad[i, j]:
                    ciclo = [np.linalg.matrix_power(P, k)[i, j] > 0 for k in range(1, n + 1)]
                    indices = [k for k, val in enumerate(ciclo, start=1) if val]
                    if indices:
                        periodos.append(np.gcd.reduce(np.diff(indices)))
        return all(p == 1 for p in periodos)
    
    resultados = {
        "filas_suman_uno": filas_suman_uno(P),
        "es_irreducible": es_irreducible(P),
        "es_aperiodica": es_aperiodica(P),
        "es_estable": False 
    }
    
    resultados["es_estable"] = all(resultados.values())
    return resultados

matrizEP1 = estadoEstable(matrizP1)
matrizEP2 = estadoEstable(matrizP2)

estadoMatrizP1 = es_matriz_estable(matrizEP1).get("es_estable")
estadoMatrizP2 = es_matriz_estable(matrizEP2).get("es_estable")

if (estadoMatrizP1 and estadoMatrizP2):
    print("\nLa matriz estable de la política #1: ")
    print(matrizEP1)

    print("\nLa matriz estable de la política #2: ")
    print(matrizEP2)

    print("\033[1m" + "Ingrese el sueldo anual que recibe un: " + "\033[0;0m")
    def sueldos(niveles):
        listaSueldos = list()
        for i in niveles:
            a = float(input(f"{i}: "))
            listaSueldos.append(a)
        return listaSueldos

    listaSueldos = np.array(sueldos(lista))

    sPromP1 = np.sum(matrizEP1[0] * listaSueldos)
    sPromP2 = np.sum(matrizEP2[0] * listaSueldos)

    def selecPolitica(sPromP1, sPromP2):
        if (sPromP1 > sPromP2):
            return f"La política #2 es más beneficiosa económicamente, la política #2: ${sPromP2} vs la política #1: ${sPromP1}."
        elif (sPromP2 > sPromP1):
            return f"La política #1 es más beneficiosa económicamente, la política #1: ${sPromP1} vs la política #2: ${sPromP2}."
        elif (sPromP1 == sPromP2):
            return f"Tanto la política #1 como la política #2 son igual de beneficiosas, ambas con un rédito de ${sPromP1}."
        
    print(f"Con respecto al análisis de selección de las políticas para la empresa {empresa} se concluyó lo siguiente: ")
    print(selecPolitica(sPromP1, sPromP2))
elif (estadoMatrizP1 == False):
    print("No se puede ejecutar el proceso, pues la matriz perteneciente a la Politica 1 no es estable, ya que: ")
    print(es_matriz_estable(matrizEP1))
elif (estadoMatrizP2 == False):
    print("No se puede ejecutar el proceso, pues la matriz perteneciente a la Politica 2 no es estable, ya que: ")
    print(es_matriz_estable(matrizEP2))