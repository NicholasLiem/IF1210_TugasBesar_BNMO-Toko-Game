#Penulis Modul: Nuha Muhammad Yahya - 16521405
#Judul Modul: Tambah Game
#Tanggal: 10 April 2022
#Deskripsi: Admin menambahkan game beserta atribut-atributnya pada program yang akan ditambahkan pada dataframe game.

import operasi_array as arr
import constant as c 


def tambah_game(data_game):
    #Bagian input atribut game
    nama = input(c.s_nameGame)
    kategori = input(c.s_categoryGame)
    tahun = input(c.s_releaseYear)
    harga = input(c.s_priceGame)
    stok = input(c.s_firstStock)

    #Validasi atribut tidak boleh kosong
    is_valid = (nama != "") and (kategori != "") and (tahun != "") and (harga != "") and (stok != "")

    #Jika terdapat atribut kosong atau tidak sesuai data type (tahun : integer, harga : integer, stok : integer), Admin diminta menginput atribut dengan benar
    while not is_valid or not ((arr.cekinteger(tahun) and arr.cekinteger(harga) and arr.cekinteger(stok))):
        print(c.tg_invalid)
        nama = input(c.s_nameGame)
        kategori = input(c.s_categoryGame)
        tahun = input(c.s_releaseYear)
        harga = input(c.s_priceGame)
        stok = input(c.s_firstStock)
    
    #Pendefinisian format ID game
    ID = "GAME{:04}".format((arr.panjang_baris(data_game)))
    
    #Game berhasil ditambahkan ke dataframe
    data_baru = [ID, nama, kategori, tahun, harga, stok]
    data_game = arr.fungsi_append(data_game, data_baru)
    
    print(f"Selamat! Berhasil menambahkan game {nama}.")
    return data_game
