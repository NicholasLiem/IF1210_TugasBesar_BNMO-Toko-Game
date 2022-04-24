#Penulis Modul: Nicholas Liem - 16521108
#Judul Modul: Find History From Id Year
#Tanggal: 15 April 2022
#Deskripsi: Mencari riyawat game diberikan id game atau tahun rilis atau tidak keduanya.
#           Jika diberikan id game maka akan diberikan data dari game_id (unik tersebut)
#           Jika diberikan hanya tahun rilis, maka akan diberikan data semua game yang dirilis pada tahun tersebut
#           Jika tidak diberikan id game ataupun tahun rilisnya maka akan diberikan seluruh data game yang tersedia
#           Jika diberikan id game dan tahun rilisnya bersamaan tetapi tidak cocok dengan data yang tersimpan, maka akan diberi pesan kesalahan,
#           tetapi jika diberikan id game dan tahun rilisnya sesuai dengan data yang tersimpan, maka akan diberikan data pada spesifiaksi tersebut.

import operasi_array as arr
import constant as c

def search_my_game(data_kepemilikan, data_game, username):
    #seach_my_game() menerima input (id_game atau tahun_rilis atau tidak keduanya) 
    #dan mengeluarkan output yang diminta.
    sliced_header = arr.delete_column(data_game, c.csvID_game_stock)[0]

    id_game = input(c.s_idGame)
    tahun_rilis = input(c.s_releaseYear)
    data_kepemilikan_user = arr.all_valid_row(data_kepemilikan, c.csvID_kepemilikan_user_id, username)

    baris_game_user = [sliced_header]
    for item in data_kepemilikan_user:
        row_id = arr.find_row_id(data_game, c.csvID_game_id, item[c.csvID_kepemilikan_game_id])
        baris_game = data_game[row_id]
        baris_game_user = arr.fungsi_append(baris_game_user, baris_game)

    if baris_game_user == [sliced_header]:
        print(c.s_notFound)
    else:
        print(c.s_listing)

        #Pembagian kasus
        if (id_game != "") or (tahun_rilis != ""): #Mengecek apakah isian semuanya kosong atau tidak

            #"Dictionary" lokal supaya mempermudah debugging dan lebih enak dilihat
            tahun_rilis_in_array = arr.found_in_kolom(baris_game_user, c.csvID_game_releaseYear, tahun_rilis)
            if tahun_rilis_in_array:
                data_baris_tahun_rilis = arr.delete_column(arr.all_valid_row(baris_game_user, c.csvID_game_releaseYear, tahun_rilis), c.csvID_game_stock)
            
            id_game_in_array = arr.found_in_kolom(baris_game_user, c.csvID_game_id, id_game)
            if id_game_in_array:
                data_baris_game_id = arr.delete_column(arr.all_valid_row(baris_game_user, c.csvID_game_id,id_game), c.csvID_game_stock)

            #Kasus pertama mengecek jika input id_game kosong
            #jika tahun yang dimasukkan merupakan bagian dari data_riwayat, maka akan diprint semua data yang berhubungan dengan tahun tsb
            if (id_game == "") and tahun_rilis_in_array:
                array_without_header = [sliced_header]
                array_without_header = arr.fungsi_append(array_without_header, data_baris_tahun_rilis[0])
                arr.cetak_tabel(array_without_header)

            #Kasus kedua mengecek jika tahun yang diisi kosong, dan mengecek jika id_game inputnya terdaftar di data_riwayat, kemudian
            #jika terdaftar di data_riwayat, akan dikeluarkan data sesuai dengan id_game yang diinput
            elif (tahun_rilis == "") and id_game_in_array:
                array_without_header = [sliced_header]
                array_without_header = arr.fungsi_append(array_without_header, data_baris_game_id[0])
                arr.cetak_tabel(array_without_header)

            #Kasus ketiga mengecek jika id_game yang diinput berada dalam data_riwayat, kemudian mengecek apakah pada baris id_game tersebut
            #tahunnya sama, jika sama maka akan dikeluarkan data berdasarkan id_game tersebut. Mengapa kasus ini dibuat?
            #Kasus ini dibuat untuk kasus di mana kedua input benar (id_game dan tahun_rilis). Kasus-kasus di atas tidak membahas jika kedua
            #variabel terisi, oleh karena itu diperlukan kasus khusus ini.
            elif id_game_in_array and (data_baris_game_id)[0][c.csvID_game_releaseYear] == tahun_rilis:
                array_without_header = [sliced_header]
                for item in data_baris_game_id:
                    array_without_header = arr.fungsi_append(array_without_header, item)
                arr.cetak_tabel(array_without_header)
                
            #Tidak memenuhi semua kasus, artinya data tidak ditemukan.
            else:
                print(c.s_notFound)

        else: #(id_game == "") and (tahun_rilis == ""). Sesuai arahan, jika tidak ada input untuk id_game dan tahun_rilis maka akan diberikan
            #semua data riwayat yang dimiliki user.
            arr.cetak_tabel(baris_game_user)
