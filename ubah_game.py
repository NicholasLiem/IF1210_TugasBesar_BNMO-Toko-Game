#Penulis Modul: Nuha Muhammad Yahya - 16521405
#Judul Modul: Ubah Game
#Tanggal: 19 April 2022
#Deskripsi: Admin mengubah atribut game pada toko game dengan input game ID, 
#           lalu admin menginput atribut barunya jika ingin diubah atau dibiarkan kosong jika tidak ingin diubah.
import operasi_array as arr
import constant as c


def ubah_game(data_game):
    #Bagian input ID game
    id = input(c.s_idGame)
    #Program mengecek apakah input game ID valid
    row_id = arr.find_row_id(data_game, c.csvID_game_id, id)

    #Jika valid, program meminta input atribut yang ingin diubah
    if arr.found_in_kolom(data_game, c.csvID_game_id, id):
        new_name = input(c.s_nameGame)
        new_category = input(c.s_categoryGame)
        new_year = input(c.s_releaseYear)
        new_price = input(c.s_priceGame)

        new_data = [id, new_name, new_category, new_year, new_price]

        #Validasi atribut "Tahun Rilis" dan "Harga Game" harus berupa integer, lalu diminta untuk mengisi inputan atribut kembali
        while not (arr.cekinteger(new_year) and arr.cekinteger(new_price)):
            print(c.tg_invalid)
            new_name = input(c.s_nameGame)
            new_category = input(c.s_categoryGame)
            new_year = input(c.s_releaseYear)
            new_price = input(c.s_priceGame)

        #Jika input atribut dikosongkan, program tidak mengubah atribut tersebut
        temp = arr.copy(data_game[row_id])
        for i in range(5):
            if new_data[i] != "":
                temp[i] = new_data[i]
                data_game[row_id] = temp

    else:
        print(c.s_notFound)
    
    return data_game
