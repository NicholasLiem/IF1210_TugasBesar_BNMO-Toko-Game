#Fungsi dan prosedur
def panjang_baris(array_data):
    panjangBaris = 0
    for baris in array_data:
        panjangBaris +=1
    return panjangBaris

def panjang_kolom(array):
    panjangKolom = 0
    for kolom in array[0]:
        panjangKolom+=1
    return panjangKolom

def fungsi_append(array,s):
    list = ['' for i in range(panjang_baris(array)+1)]
    for i in range (panjang_baris(array)+1):
        if i < panjang_baris (array):
            list[i]=array[i]
        else:
            list[i]=s
    return list

def copy(array):
    tmp = ['' for _ in range(panjang_baris(array))]
    for i in range(panjang_baris(array)):
        tmp[i] = array[i]
    return tmp

def join(s, array_string):
    out = ''
    panjang = panjang_baris(array_string)
    for i in range(panjang-1):
        out += array_string[i] + s
    out += array_string[panjang-1]
    return out

#SEARCHING
def found_in_kolom(array,kolom_id,validator):
    found = False
    for i in range(panjang_baris(array)):
        if array[i][kolom_id] == validator:
            found = True
    if found == True:
        return True
    else:
        return False

def all_valid_row(array,csvID,validator):
    data_baris = []
    for baris in array:
        if baris[csvID] == validator:
            data_baris = fungsi_append(data_baris, baris)
    return data_baris

def find_row_id(array, csvID, validator):
    #Asumsikan bahwa data pasti ada di barisnya
    panjang_baris_data = panjang_baris(array)
    for i in range(1,panjang_baris_data,1):
        if array[i][csvID] == validator:
            baris_id = i
    return baris_id

def delete_column(array, columnCSVId):
    panjang_kolom_data = panjang_kolom(array)
    array_without_column = []
    for item in array:
        baris_temp = []
        for i in range(panjang_kolom_data):
            if i != columnCSVId:
                baris_temp = fungsi_append(baris_temp,item[i])
        array_without_column = fungsi_append(array_without_column, baris_temp)
    return array_without_column