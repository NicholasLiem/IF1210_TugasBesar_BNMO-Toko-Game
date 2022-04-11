import parseran
import operasi_array as arr

path = "Data/game.csv"

def tambah_game():
    data_game = parseran.csv_to_matrix(path)

    nama = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    while tahun_rilis != "" and type(tahun_rilis) != int:
        tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")

    stok = input("Masukkan stok awal: ")
    ID = "GAME{:04}".format((arr.panjang_baris(data_game)))
    
    data_baru = [ID, nama, kategori, tahun_rilis, harga, stok]
    data_baru = arr.fungsi_append(data_game, data_baru)
    parseran.matrix_to_csv(path, data_baru)

tambah_game()