#Penulis Modul: Nicholas Liem - 16521108
#Judul Modul: List Game
#Tanggal: 17 April 2022

import operasi_array as arr
import constant as c

def list_game_toko(data_game):
    temp = arr.copy(data_game)
    skema = input(c.sl_skema)
    if skema == "tahun+":
        sorted_data = arr.sorting_ascd(temp,c.csvID_game_releaseYear)
        arr.cetak_tabel(sorted_data)
    elif skema == "tahun-":
        sorted_data = arr.sorting_dscd(temp,c.csvID_game_releaseYear)
        arr.cetak_tabel(sorted_data)
    elif skema == "harga-":
        sorted_data = arr.sorting_dscd(temp,c.csvID_game_price)
        arr.cetak_tabel(sorted_data)
    elif skema == "harga+":
        sorted_data = arr.sorting_ascd(temp,c.csvID_game_price)
        arr.cetak_tabel(sorted_data)
    elif skema == "":
        arr.cetak_tabel(temp)
    else:
        print(c.sl_invalid)