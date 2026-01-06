from kurushima import fillsquare, printsquare
import math

def verifysquare(square):
    sums = []
    rowsums = [sum(square[i]) for i in range(0,len(square))]
    sums.append(rowsums)

    colsums = [sum([row[i] for row in square]) for i in
    range(0,len(square))]
    sums.append(colsums)

    maindiag = sum([square[i][i] for i in range(0,len(square))])
    sums.append([maindiag])

    antidiag = sum([square[i][len(square) - 1 - i] for i in range(0,len(square))])
    sums.append([antidiag])

    flattened = [j for i in sums for j in i]
    return(len(list(set(flattened))) == 1)


n = 11
square = [[float("nan") for i in range(0, n)] for j in range(0, n)]

center_i = math.floor(n/2)
center_j = math.floor(n/2)

square[center_i][center_j] = int((n**2 + 1) / 2)
square[center_i + 1][center_j] = 1
square[center_i - 1][center_j] = n**2
square[center_i][center_j + 1] = n**2 + 1 - n
square[center_i][center_j - 1] = n

entry_i = center_i
entry_j = center_j

square = fillsquare(square, entry_i, entry_j, (n**2)/2 - 4)

entry_i = math.floor(n/2) + 1
entry_j = math.floor(n/2)

square = fillsquare(square, entry_i, entry_j, 0)

square = [[n**2 if x == 0 else x for x in row] for row in square]

printsquare(square)