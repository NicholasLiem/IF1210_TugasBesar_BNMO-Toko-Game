#10 april 2022
import operasi_array as arr
import constant as c 

def tambah_game(data_game):
    nama = input(c.s_nameGame)
    kategori = input(c.s_categoryGame)
    tahun = input(c.s_releaseYear)
    harga = input(c.s_priceGame)
    stok = input(c.s_firstStock)

    is_valid = (nama != "") and (kategori != "") and (tahun != "") and (harga != "") and (stok != "")

    while not is_valid or not ((arr.cekinteger(tahun) and arr.cekinteger(harga) and arr.cekinteger(stok))):
        print(c.tg_invalid)
        nama = input(c.s_nameGame)
        kategori = input(c.s_categoryGame)
        tahun = input(c.s_releaseYear)
        harga = input(c.s_priceGame)
        stok = input(c.s_firstStock)
    
    ID = "GAME{:04}".format((arr.panjang_baris(data_game)))
    
    data_baru = [ID, nama, kategori, tahun, harga, stok]
    data_game = arr.fungsi_append(data_game, data_baru)
    print(f"Selamat! Berhasil menambahkan game {nama}.")
    return data_game
