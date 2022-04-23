#Penulis Modul: Nicholas Liem - 16521108
#Judul Modul: Find Game
#Tanggal: 10 April 2022
#Deskripsi: Mencari data game diberikan input (opsional) id, nama, kategori, releaseYear, price, dan stock.
#           Kemudian, berdasarkan input yang diberikan, akan dikeluarkan semua data yang memenuhi input.

import operasi_array as arr
import constant as c

#Data-data unik: id, nama
#Data-data umum: harga, kategori, tahun rilis
def search_game_at_store(data_game):

    #Bagian input data
    id_game = input(c.s_idGame)
    nama_game = input(c.s_nameGame)
    category_game = input(c.s_categoryGame)
    releaseYear_game = input(c.s_releaseYear)
    price_game = input(c.s_priceGame)

    #Bagian mengecek input
    found_id = arr.found_in_kolom(data_game,c.csvID_game_id, id_game)
    found_nama = arr.found_in_kolom(data_game,c.csvID_game_nama, nama_game)
    found_category = arr.found_in_kolom(data_game,c.csvID_game_kategori, category_game)
    found_releaseYear = arr.found_in_kolom(data_game,c.csvID_game_releaseYear, releaseYear_game)
    found_price = arr.found_in_kolom(data_game,c.csvID_game_price, price_game)

    #Mendaftarkan semua baris yang memiliki karakteristik berdasarkan inputnya
    row_id = arr.find_row_id(data_game, c.csvID_game_id, id_game)
    row_nama = arr.find_row_id(data_game, c.csvID_game_nama, nama_game)
    baris_kategori = arr.all_valid_row(data_game, c.csvID_game_kategori, category_game)
    baris_releaseYear = arr.all_valid_row(data_game, c.csvID_game_releaseYear, releaseYear_game)
    baris_price = arr.all_valid_row(data_game, c.csvID_game_price, price_game)

    array_input = [id_game,nama_game,category_game,releaseYear_game, price_game]

    flag = False

    #Proses pembagian kasus
    if id_game == "" and nama_game == "" and price_game == "" and category_game == "" and releaseYear_game == "":
        arr.cetak_tabel(data_game)

    else:
        print(c.s_listing)

        #Kasus game_id yang diinput benar, kalau sisanya salah, maka tidak akan dikeluarkan data
        if found_id:
            for i in range (4):
                if (data_game[row_id][i] != array_input[i]) and array_input[i] != "":
                    flag = True
            if flag == False:
                arr.cetak_tabel([data_game[row_id]])
            else:
                print(c.s_notFound)

        #Kasus nama game yang diinput benar, kalau sisanya salah, maka tidak akan dikeluarkan data
        elif found_nama:
            for i in range (4):
                if data_game[row_nama][i] != array_input[i] and array_input[i] != "":
                    flag = True
            if flag == False:
                arr.cetak_tabel([data_game[row_id]])
            else:
                print (c.s_notFound)

        #Kasus tiga parameter semua benar
        else:
            if found_price and found_category and found_releaseYear:
                if arr.operasi_dua_array(baris_price, baris_kategori, "CHECK_IF_CONSISTS") and arr.operasi_dua_array(baris_kategori, baris_releaseYear, "CHECK_IF_CONSISTS") and arr.operasi_dua_array(baris_price, baris_releaseYear, "CHECK_IF_CONSISTS"):
                    array_temp = [data_game[0]]
                    for item in baris_price:
                        for items in baris_kategori:
                            for itemss in baris_releaseYear:
                                if item == items == itemss:
                                    array_temp = arr.fungsi_append(array_temp, item)
                    arr.cetak_tabel(array_temp)
                else:
                    print(c.s_notFound)

            #Kasus 2 benar, satu salah
            elif found_price and found_category and not found_releaseYear:
                if arr.operasi_dua_array(baris_price, baris_kategori, "CHECK_IF_CONSISTS"):
                    arr.cetak_tabel(arr.operasi_dua_array(baris_price, baris_kategori, "RETURN_SAME"))
                else:
                    print(c.s_notFound)

            elif found_price and not found_category and found_releaseYear:
                if arr.operasi_dua_array(baris_price, baris_releaseYear, "CHECK_IF_CONSISTS"):
                    arr.cetak_tabel(arr.operasi_dua_array(baris_price, baris_releaseYear, "RETURN_SAME"))
                else:
                    print(c.s_notFound)

            elif not found_price and found_category and found_releaseYear:
                if arr.operasi_dua_array(baris_kategori, baris_releaseYear, "CHECK_IF_CONSISTS"):
                    arr.cetak_tabel(arr.operasi_dua_array(baris_kategori, baris_releaseYear, "RETURN_SAME"))
                else:
                    print(c.s_notFound)

            #Kasus 1 benar, 2 salah
            elif found_price and not found_category and not found_releaseYear:
                arr.cetak_tabel(baris_price)

            elif not found_price and found_category and not found_releaseYear:
                arr.cetak_tabel(baris_kategori)

            elif not found_price and not found_category and found_releaseYear:
                arr.cetak_tabel(baris_releaseYear)
                
            else:
                print(c.s_notFound)
