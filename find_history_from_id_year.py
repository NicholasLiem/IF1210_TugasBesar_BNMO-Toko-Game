#Penulis Modul: Nicholas Liem - 16521108
#Judul Modul: Find History From Id Year
#Versi Modul: 1.0
#Tanggal: 9 April 2022
#Deskripsi: Mencari riyawat game diberikan id game atau tahun rilis atau tidak keduanya.
#           Jika diberikan id game maka akan diberikan data dari game_id (unik tersebut)
#           Jika diberikan hanya tahun rilis, maka akan diberikan data semua game yang dibeli pada tahun tersebut
#           Jika tidak diberikan id game ataupun tahun rilisnya maka akan diberikan seluruh data game yang tersedia
#           Jika diberikan id game dan tahun rilisnya bersamaan tetapi tidak cocok dengan data yang tersimpan, maka akan diberi pesan kesalahan,
#           tetapi jika diberikan id game dan tahun rilisnya sesuai dengan data yang tersimpan, maka akan diberikan data pada spesifiaksi tersebut.

#Import modul-modul yang diperlukan
import operasi_array as arr
import parseran
import constant as c

#Konstanta/"Dictionary"
#Berfungsi untuk mengubah variabel dengan lebih mudah karena "tersimpan" pada satu tempat yang sama
dir = "Data/riwayat.csv"

#Import data dari csv ke dalam bentuk matriks bernama "data_riwayat" supaya bisa diakses dengan mudah
data_riwayat = parseran.csv_to_matrix(dir)

#Multipurpose function
def array_function(array, csv_col_id, validator, function):
    if function == "CHECK": #Mengecek apakah id game atau tahun rilis berada pada data di array data_riwayat
        #                    Mengeluarkan nilai true jika ada, jika tidak ada maka mengeluarkan false.
        found = False
        for baris in array:
            if baris[csv_col_id] == validator:
                found = True
        if found == False:
            return False
        else:
            return True

    elif function == "DATA_BARIS": #Memberikan data baris diberikan id game atau tahun rilis, tetapi di sini hanya digunakan untuk
        #                           id game karena id game unik, jadi pasti memberikan nilai pertama dan satu-satunya nilai. Kalau tahun rilis bisa beda-beda
        data_baris = []
        #Skema searching
        for baris in array:
            if baris[csv_col_id] == validator:
                data_baris = baris
        return data_baris

    elif function == "PRINT_DATA": #Melakukan print data baris dalam bentuk penampilan tertentu
        num = 1
        for baris in array:
            if baris[csv_col_id] == validator:
                print(f"{num}. ", end = "")
                for item in baris:
                    print(item, end = " | ") 
                num += 1
                print("")

    else: #Kasus yang tidak mungkin terjadi
        print(c.s_error)

#komentarin ini
def search_my_game():
    #seach_my_game() merupakan fungsi utama dalam modul ini. Fungsi ini menerima input (id_game atau release_year atau tidak keduanya) 
    #dan mengeluarkan output yang diminta.

    id_game = input(c.s_idGame)
    release_year = input(c.s_releaseYear)
    print(c.s_listing)

    #Pembagian kasus
    if (id_game != "") or (release_year != ""): #Mengecek apakah isian semuanya kosong atau tidak

        #"Dictionary" lokal supaya mempermudah debugging dan lebih enak dilihat
        release_year_in_array = array_function(data_riwayat,c.csvID_riwayat_releaseYear, release_year, "CHECK")
        id_game_in_array = array_function(data_riwayat,c.csvID_riwayat_id,id_game, "CHECK")
        data_baris_game_id = array_function(data_riwayat, c.csvID_riwayat_id, id_game,"DATA_BARIS")

        #Kasus pertama mengecek jika input id_game kosong atau ada tetapi tidak terdaftar di data_riwayat kemudian
        #jika tahun yang dimasukkan merupakan bagian dari data_riwayat, maka akan diprint semua data yang berhubungan dengan tahun tsb
        if (id_game == "" or not(id_game_in_array)) and release_year_in_array:
            array_function(data_riwayat,c.csvID_riwayat_releaseYear,release_year, "PRINT_DATA")

        #Kasus kedua mengecek jika tahun yang diisi kosong, dan mengecek jika id_game inputnya terdaftar di data_riwayat, kemudian
        #jika terdaftar di data_riwayat, akan dikeluarkan data sesuai dengan id_game yang diinput
        elif release_year == "" and id_game_in_array:
            array_function(data_riwayat,c.csvID_riwayat_riwayat_id,id_game, "PRINT_DATA")

        #Kasus ketiga mengecek jika id_game yang diinput berada dalam data_riwayat, kemudian mengecek apakah pada baris id_game tersebut
        #tahunnya sama, jika sama maka akan dikeluarkan data berdasarkan id_game tersebut. Mengapa kasus ini dibuat?
        #Kasus ini dibuat untuk kasus di mana kedua input benar (id_game dan release_year). Kasus-kasus di atas tidak membahas jika kedua
        #variabel terisi, oleh karena itu diperlukan kasus khusus ini.
        elif not(data_baris_game_id == []) and (data_baris_game_id)[c.csvID_riwayat_releaseYear] == release_year:
            array_function(data_riwayat,c.csvID_riwayat_id,id_game, "PRINT_DATA")

        #Tidak memenuhi semua kasus, artinya data tidak ditemukan.
        else:
            print(c.s_notFound)

    else: #(id_game == "") and (release_year == ""). Sesuai arahan, jika tidak ada input untuk id_game dan release_year maka akan diberikan
        #semua data riwayat yang dimiliki user.
        for baris in range(1,arr.panjang_baris(data_riwayat)):
            print(data_riwayat[baris]) #Perlu dibenerin prinannya