import parseran
import operasi_array as arr
import constant as c

path = "Data/game.csv"
data_game = parseran.csv_to_matrix(path)

def cekinteger(variabel):
    for c in variabel:
        if not(48 <= ord(c) <= 57):
            return False
    return True 

def isvalid(inputs):
    for i in range(5):
        if inputs[i] == "":
            return False
    return True

def masukkan():
    nama = input(c.s_nameGame)
    kategori = input(c.s_categoryGame)
    tahun = input(c.s_releaseYear)
    harga = input(c.s_priceGame)
    stok = input(c.s_firstStock)
    return nama, kategori, tahun, harga, stok

def tambah_game():
    inputs = masukkan()
    while not isvalid(inputs) or not ((cekinteger(inputs[2]) and cekinteger(inputs[3]) and cekinteger(inputs[4]))):
        print(c.tg_invalid)
        inputs = masukkan()
      
    ID = "GAME{:04}".format((arr.panjang_baris(data_game)))
    
    data_baru = [ID, inputs[0], inputs[1], inputs[2], inputs[3], inputs[4]]
    data_baru = arr.fungsi_append(data_game, data_baru)
    parseran.matrix_to_csv(path, data_baru)
