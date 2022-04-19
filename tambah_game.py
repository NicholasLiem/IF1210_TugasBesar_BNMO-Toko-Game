#10 april 2022
import operasi_array as arr
import constant as c

def cekinteger(variabel):
    for c in variabel:
        if not(48 <= ord(c) <= 57):
            return False
    return True 

def tambah_game(data_game):
    nama = input(c.s_nameGame)
    kategori = input(c.s_categoryGame)
    tahun = input(c.s_releaseYear)
    harga = input(c.s_priceGame)
    stok = input(c.s_firstStock)

    is_valid = (nama != "") and (kategori != "") and (tahun != "") and (harga != "") and (stok != "")

    while not is_valid or not ((cekinteger(tahun) and cekinteger(harga) and cekinteger(stok))):
        print(c.tg_invalid)
        nama = input(c.s_nameGame)
        kategori = input(c.s_categoryGame)
        tahun = input(c.s_releaseYear)
        harga = input(c.s_priceGame)
        stok = input(c.s_firstStock)
    
    ID = "GAME{:04}".format((arr.panjang_baris(data_game)))
    
    data_baru = [ID, inputs[0], inputs[1], inputs[2], inputs[3], inputs[4]]
    data_baru = arr.fungsi_append(data_game, data_baru)
    return data_baru

