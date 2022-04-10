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

def join(s, array_string):
    out = ''
    panjang = panjang_baris(array_string)
    for i in range(panjang-1):
        out += array_string[i] + s
    out += array_string[panjang-1]
    return out

#SEARCHING
def search_in_kolom(array,kolom_id,validator):
    found = False
    for i in range(panjang_baris(array)):
        if array[i][kolom_id] == validator:
            found = True
    if found == True:
        return True
    else:
        return False
