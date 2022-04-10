#Penulis Modul: Nicholas Liem - 16521108
#Judul Modul: Find Game
#Versi Modul: 1.0
#Tanggal: 10 April 2022
#Deskripsi: Mencari data game diberikan input (opsional) id, nama, kategori, releaseYear, price, dan stock.
#           Kemudian, berdasarkan input yang diberikan, akan dikeluarkan semua data yang memenuhi input.

#Import modul-modul yang diperlukan
import operasi_array as arr
import constant as c
import parseran

#Konstanta/"Dictionary"
#Berfungsi untuk mengubah variabel dengan lebih mudah karena "tersimpan" pada satu tempat yang sama
dir = "Data/game.csv"

#Mendifinisikan array yang akan dipakai
data_game = parseran.csv_to_matrix(dir)
#Data-data unik: id, nama
#Data-data umum: harga, kategori, tahun rilis

def input_checker(id_game, nama_game, price_game, category_game, releaseYear_game):
    found_id = False
    found_nama = False
    found_price = False
    found_category = False
    found_releaseYear = False
   
    found_id = found_in_kolom(data_game,c.csvID_id, id_game)
    found_nama = found_in_kolom(data_game,c.csvID_nama, nama_game)
    found_price = found_in_kolom(data_game,c.csvID_price, price_game)
    found_category = found_in_kolom(data_game,c.csvID_kategori, category_game)
    found_releaseYear = found_in_kolom(data_game,c.csvID_releaseYear, releaseYear_game)
    
    return found_id, found_nama, found_price, found_category, found_releaseYear

def found_in_kolom(array,kolom_id,validator):
    found = False
    panjang_baris_data = arr.panjang_baris(array)
    for i in range(panjang_baris_data):
        if array[i][kolom_id] == validator:
            found = True
    if found == True:
        return True
    else:
        return False

def all_valid_row(array,csvID,validator):
    data_baris = []
    for baris in array:
        if baris[csvID] == validator:
            data_baris = arr.fungsi_append(data_baris, baris)
    return data_baris

#Multipurpose array
def operasi_array(array1, array2, operator):
    array_sama = []
    found = False
    if operator == "CHECK_IF_CONSISTS":
        for item1 in array1:
            for item2 in array2:
                if item1 == item2:
                    found = True
        return found

    elif operator == "RETURN_SAME":
        for item1 in array1:
            for item2 in array2:
                if item1 == item2:
                    array_sama = arr.fungsi_append(array_sama,item1)
        return array_sama

def search_game_at_store():

    #Bagian input data
    id = input(c.s_idGame)
    nama = input(c.s_nameGame)
    price = input(c.s_priceGame)
    category = input(c.s_categoryGame)
    releaseYear = input(c.s_releaseYear)

    #Bagian mengecek input
    checklist = input_checker(id, nama, price, category, releaseYear)

    id_check = checklist[0]
    nama_check = checklist[1]
    price_check = checklist[2]
    category_check = checklist[3]
    releaseYear_check = checklist[4]

    #Mendaftarkan semua baris yang memiliki karakteristik berdasarkan inputnya
    baris_id = all_valid_row(data_game, c.csvID_id, id)
    baris_nama = all_valid_row(data_game, c.csvID_nama, nama)
    baris_price = all_valid_row(data_game, c.csvID_price, price)
    baris_kategori = all_valid_row(data_game, c.csvID_kategori, category)
    baris_releaseYear = all_valid_row(data_game, c.csvID_releaseYear, releaseYear)

    #Proses pembagian kasus
    if id == "" and nama == "" and price == "" and category == "" and releaseYear == "":
        for baris in range(1,arr.panjang_baris(data_game)):
            print(data_game[baris])
    else:
        print(c.s_listing)
        if id_check and nama_check:
            if baris_id == baris_nama:
                print(baris_id)
            else:
                print(c.s_notFound)
        elif id_check and nama == "":
            print(baris_id)
        elif id == "" and nama_check:
            print(baris_nama)

        #Print semua baris
        #Kasus semua benar
        elif price_check and category_check and releaseYear_check:
            if operasi_array(baris_price, baris_kategori, "CHECK_IF_CONSISTS") and operasi_array(baris_kategori, baris_releaseYear, "CHECK_IF_CONSISTS") and operasi_array(baris_price, baris_releaseYear, "CHECK_IF_CONSISTS"):
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
        elif price_check and category_check and not releaseYear_check:
            if operasi_array(baris_price, baris_kategori, "CHECK_IF_CONSISTS"):
                print(operasi_array(baris_price, baris_kategori, "RETURN_SAME"))
            else:
                print(c.s_notFound)

        elif price_check and not category_check and releaseYear_check:
            if operasi_array(baris_price, baris_releaseYear, "CHECK_IF_CONSISTS"):
                print(operasi_array(baris_price, baris_releaseYear, "RETURN_SAME"))
            else:
                print(c.s_notFound)

        elif not price_check and category_check and releaseYear_check:
            if operasi_array(baris_kategori, baris_releaseYear, "CHECK_IF_CONSISTS"):
                print(operasi_array(baris_kategori, baris_releaseYear, "RETURN_SAME"))
            else:
                print(c.s_notFound)

        #Kasus 1 benar, 2 salah
        elif price_check and not category_check and not releaseYear_check:
            print(baris_price)

        elif not price_check and category_check and not releaseYear_check:
            print(baris_kategori)

        elif not price_check and not category_check and releaseYear_check:
            print(baris_releaseYear)
            
        else:
            print(c.s_notFound)

#search_game_at_store()