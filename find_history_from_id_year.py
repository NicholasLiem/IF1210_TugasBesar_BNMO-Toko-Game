#Penulis Modul: Nicholas Liem - 16521108
#Judul Modul: Find History From Id Year
#Tanggal: 19 April 2022
#Deskripsi: Mencari riyawat game diberikan id game atau tahun rilis atau tidak keduanya.
#           Jika diberikan id game maka akan diberikan data dari game_id (unik tersebut)
#           Jika diberikan hanya tahun rilis, maka akan diberikan data semua game yang dibeli pada tahun tersebut
#           Jika tidak diberikan id game ataupun tahun rilisnya maka akan diberikan seluruh data game yang tersedia
#           Jika diberikan id game dan tahun rilisnya bersamaan tetapi tidak cocok dengan data yang tersimpan, maka akan diberi pesan kesalahan,
#           tetapi jika diberikan id game dan tahun rilisnya sesuai dengan data yang tersimpan, maka akan diberikan data pada spesifiaksi tersebut.

#Import modul-modul yang diperlukan
import operasi_array as arr
import constant as c

def search_my_game(data_riwayat, username):
    #seach_my_game() merupakan fungsi utama dalam modul ini. Fungsi ini menerima input (id_game atau tahun_beli atau tidak keduanya) 
    #dan mengeluarkan output yang diminta.

    id_game = input(c.s_idGame)
    tahun_beli = input(c.s_releaseYear)
    data_riwayat_user = arr.all_valid_row(data_riwayat, c.csvID_riwayat_username, username)
    print(c.s_listing)

    #Pembagian kasus
    if (id_game != "") or (tahun_beli != ""): #Mengecek apakah isian semuanya kosong atau tidak

        #"Dictionary" lokal supaya mempermudah debugging dan lebih enak dilihat
        tahun_beli_in_array = arr.found_in_kolom(data_riwayat_user, c.csvID_riwayat_tahun_beli, tahun_beli)
        if tahun_beli_in_array:
            data_baris_tahun_beli = arr.all_valid_row(data_riwayat_user, c.csvID_riwayat_tahun_beli, tahun_beli)
            data_baris_tahun_beli_without_username = arr.delete_column(data_baris_tahun_beli, c.csvID_riwayat_username)
        else:
            data_baris_tahun_beli = []
            data_baris_tahun_beli_without_username = []
        
        id_game_in_array = arr.found_in_kolom(data_riwayat_user, c.csvID_riwayat_game_id, id_game)
        if id_game_in_array:
            data_baris_game_id = arr.all_valid_row(data_riwayat_user, c.csvID_riwayat_game_id,id_game)
            data_baris_game_without_username = arr.delete_column(data_baris_game_id, c.csvID_riwayat_username)
        else:
            data_baris_game_id = []
            data_baris_game_without_username = []

        print(data_baris_game_id)

        #Kasus pertama mengecek jika input id_game kosong
        #jika tahun yang dimasukkan merupakan bagian dari data_riwayat, maka akan diprint semua data yang berhubungan dengan tahun tsb
        if (id_game == "") and tahun_beli_in_array:
            arr.cetak_tabel(data_baris_tahun_beli_without_username)

        #Kasus kedua mengecek jika tahun yang diisi kosong, dan mengecek jika id_game inputnya terdaftar di data_riwayat, kemudian
        #jika terdaftar di data_riwayat, akan dikeluarkan data sesuai dengan id_game yang diinput
        elif (tahun_beli == "") and id_game_in_array:
            arr.cetak_tabel(data_baris_game_without_username)

        #Kasus ketiga mengecek jika id_game yang diinput berada dalam data_riwayat, kemudian mengecek apakah pada baris id_game tersebut
        #tahunnya sama, jika sama maka akan dikeluarkan data berdasarkan id_game tersebut. Mengapa kasus ini dibuat?
        #Kasus ini dibuat untuk kasus di mana kedua input benar (id_game dan tahun_beli). Kasus-kasus di atas tidak membahas jika kedua
        #variabel terisi, oleh karena itu diperlukan kasus khusus ini.
        elif id_game_in_array and (data_baris_game_id)[0][c.csvID_riwayat_tahun_beli] == tahun_beli:
            arr.cetak_tabel(data_baris_game_without_username)
            
        #Tidak memenuhi semua kasus, artinya data tidak ditemukan.
        else:
            print(c.s_notFound)

    else: #(id_game == "") and (tahun_beli == ""). Sesuai arahan, jika tidak ada input untuk id_game dan tahun_beli maka akan diberikan
        #semua data riwayat yang dimiliki user.
        arr.cetak_tabel(data_riwayat_user)