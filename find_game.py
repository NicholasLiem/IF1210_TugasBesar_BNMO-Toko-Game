#Penulis Modul: Nicholas Liem - 16521108
#Judul Modul: Find Game
#Versi Modul: 1.0
#Tanggal: 10 April 2022
#Deskripsi: Mencari data game diberikan input (opsional) id, nama, kategori, releaseYear, price, dan stock.
#           Kemudian, berdasarkan input yang diberikan, akan dikeluarkan semua data yang memenuhi input.

#Import modul-modul yang diperlukan
import operasi_array as arr
import constant as c

#Data-data unik: id, nama
#Data-data umum: harga, kategori, tahun rilis

#Multipurpose array
def search_game_at_store(data_game):

    #Bagian input data
    id_game = input(c.s_idGame)
    nama_game = input(c.s_nameGame)
    price_game = input(c.s_priceGame)
    category_game = input(c.s_categoryGame)
    releaseYear_game = input(c.s_releaseYear)

    #Bagian mengecek input
    found_id = arr.found_in_kolom(data_game,c.csvID_game_id, id_game)
    found_nama = arr.found_in_kolom(data_game,c.csvID_game_nama, nama_game)
    found_price = arr.found_in_kolom(data_game,c.csvID_game_price, price_game)
    found_category = arr.found_in_kolom(data_game,c.csvID_game_kategori, category_game)
    found_releaseYear = arr.found_in_kolom(data_game,c.csvID_game_releaseYear, releaseYear_game)

    #Mendaftarkan semua baris yang memiliki karakteristik berdasarkan inputnya
    baris_id = arr.all_valid_row(data_game, c.csvID_game_id, id_game)
    baris_nama = arr.all_valid_row(data_game, c.csvID_game_nama, nama_game)
    baris_price = arr.all_valid_row(data_game, c.csvID_game_price, price_game)
    baris_kategori = arr.all_valid_row(data_game, c.csvID_game_kategori, category_game)
    baris_releaseYear = arr.all_valid_row(data_game, c.csvID_game_releaseYear, releaseYear_game)

    #Proses pembagian kasus
    if id_game == "" and nama_game == "" and price_game == "" and category_game == "" and releaseYear_game == "":
        for baris in range(1,arr.panjang_baris(data_game)):
            print(data_game[baris])
    else:
        print(c.s_listing)
        if found_id and found_nama:
            if baris_id == baris_nama:
                print(baris_id)
            else:
                print(c.s_notFound)
        elif found_id and nama_game == "":
            print(baris_id)
        elif id == "" and found_nama:
            print(baris_nama)

        #Print semua baris
        #Kasus semua benar
        elif found_price and found_category and found_releaseYear:
            if operasi_dua_array(baris_price, baris_kategori, "CHECK_IF_CONSISTS") and operasi_dua_array(baris_kategori, baris_releaseYear, "CHECK_IF_CONSISTS") and operasi_dua_array(baris_price, baris_releaseYear, "CHECK_IF_CONSISTS"):
                array_temp = []
                for item in baris_price:
                    for items in baris_kategori:
                        for itemss in baris_releaseYear:
                            if item == items == itemss:
                                array_temp = arr.fungsi_append(array_temp, item)
                print(array_temp)
            else:
                print(c.s_notFound)

        #Kasus 2 benar, satu salah
        elif found_price and found_category and not found_releaseYear:
            if operasi_dua_array(baris_price, baris_kategori, "CHECK_IF_CONSISTS"):
                print(operasi_dua_array(baris_price, baris_kategori, "RETURN_SAME"))
            else:
                print(c.s_notFound)

        elif found_price and not found_category and found_releaseYear:
            if operasi_dua_array(baris_price, baris_releaseYear, "CHECK_IF_CONSISTS"):
                print(operasi_dua_array(baris_price, baris_releaseYear, "RETURN_SAME"))
            else:
                print(c.s_notFound)

        elif not found_price and found_category and found_releaseYear:
            if operasi_dua_array(baris_kategori, baris_releaseYear, "CHECK_IF_CONSISTS"):
                print(operasi_dua_array(baris_kategori, baris_releaseYear, "RETURN_SAME"))
            else:
                print(c.s_notFound)

        #Kasus 1 benar, 2 salah
        elif found_price and not found_category and not found_releaseYear:
            print(baris_price)

        elif not found_price and found_category and not found_releaseYear:
            print(baris_kategori)

        elif not found_price and not found_category and found_releaseYear:
            print(baris_releaseYear)
            
        else:
            print(c.s_notFound)