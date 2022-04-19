import operasi_array as arr

def split_csv(line):
    out = []
    tmp = ''
    for c in line:
        if c == ';':
            out = arr.fungsi_append(out, tmp)
            tmp = ''
        else:
            if c != '\n':
                tmp += c
    out = arr.fungsi_append(out, tmp)
    return out

def tambah_data(path, line):
    with open(path, 'a+') as csv:
        if arr.panjang_baris(split_csv(line)) != arr.panjang_baris(split_csv(csv.readline())):
            raise ValueError('Banyak data tidak sesuai')
        csv.write('\n' + line)

def matrix_to_csv(path, matrix):
    with open(path, 'w') as csv:
        panjang = arr.panjang_baris(matrix)
        for i in range(panjang-1):
            csv.write(arr.join(';', matrix[i]) + '\n')
        csv.write(arr.join(';', matrix[panjang-1]))

def csv_to_matrix(path):
    with open(path) as csv:
        lines = csv.readlines()
        matrix = []
        for line in lines:
            matrix = arr.fungsi_append(matrix, split_csv(line))
    return matrix
