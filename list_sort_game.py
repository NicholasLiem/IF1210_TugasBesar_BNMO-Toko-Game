import operasi_array as arr
import constant as c
# import parseran

def list_game_toko(data_game):
    skema = input(c.sl_skema)
    if skema == "tahun-":
        sorted_data = arr.sorting_low(data_game,c.csvID_game_releaseYear)
        arr.cetak_tabel(sorted_data)
    elif skema == "tahun+":
        sorted_data = arr.sorting_high(data_game,c.csvID_game_releaseYear)
        arr.cetak_tabel(sorted_data)
    elif skema == "harga+":
        sorted_data = arr.sorting_high(data_game,c.csvID_game_price)
        arr.cetak_tabel(sorted_data)
    elif skema == "harga-":
        sorted_data = arr.sorting_low(data_game,c.csvID_game_price)
        arr.cetak_tabel(sorted_data)
    else:
        arr.cetak_tabel(data_game)

# data_game = parseran.csv_to_matrix("Data/game.csv")
# list_game_toko(data_game)