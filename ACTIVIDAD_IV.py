def hay_conflicto(row, col):
    for i in range(col):
        if row[i] == row[col] or abs(row[i] - row[col]) == col - i:
            return True
    return False

def cuatro_reinas(row):
    k = 0
    row[k] = 0
    while k >= 0:
        row[k] += 1
        while row[k] <= 4 and hay_conflicto(row, k):
            row[k] += 1
        if row[k] <= 4:
            if k == 3:
                return True
            k += 1
            row[k] = 0
        else:
            k -= 1
    return False

# Crea un arreglo de tamaño 4 con las posiciones iniciales de las reinas
row = [0, 0, 0, 0]

# Llama a la función y pasa el arreglo creado como argumento
solucion = cuatro_reinas(row)

# Muestra la solución encontrada
if solucion:
    print("Se encontro una solucion:", row)
else:
    print("No se encontro solucion")
