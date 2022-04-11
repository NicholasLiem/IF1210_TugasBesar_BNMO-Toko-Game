import parseran
import operasi_array as arr

def max_in_row(matrix, index, context):
    maks = matrix[index][0]
    for i in range(arr.panjang_kolom(matrix)):
        if context(maks) < context(matrix[index][i]):
            maks = matrix[index][i]
    return maks

def max_in_column(matrix, index, context):
    maks = matrix[0][index]
    for i in range(arr.panjang_baris(matrix)):
        if context(maks) < context(matrix[i][index]):
            maks = matrix[i][index]
    return maks

def cetak_tabel(matrix):
    kolom = arr.panjang_kolom(matrix)
    baris = arr.panjang_baris(matrix)
    max_width = [0 for x in range(kolom)]
    pemisah = '+'
    for i in range(kolom):
        max_width[i] = arr.panjang_baris(max_in_column(matrix, i, arr.panjang_baris))
        pemisah += '-' * max_width[i] + '+'
    for i in range(baris):
        print(pemisah)
        for j in range(kolom):
            if i == 0:
                print("|\x1b[1m{0:^{width}}\x1b[0m".format(matrix[i][j], width=max_width[j]), end='')                
            else:
                print("|{0:<{width}}".format(matrix[i][j], width=max_width[j]), end='')
        print('|')
    print(pemisah)