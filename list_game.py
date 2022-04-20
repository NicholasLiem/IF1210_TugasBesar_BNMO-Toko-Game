import operasi_array as arr
import constant as c

def list_game(data_game, data_kepemilikan, username):
    if not(arr.found_in_kolom(data_kepemilikan, c.csvID_kepemilikan_user_id, username)):
    #Artinya user belum pernah membeli game, akan dikeluarkan teks bahwa tidak ada riwayat game pada user
        print(c.l_notFound)
        
    else:
        list_game = []
        game_id_kepemilikan_user = arr.all_valid_row(data_kepemilikan, c.csvID_kepemilikan_user_id, username)
        
        for item in game_id_kepemilikan_user:
            game_id = item[c.csvID_kepemilikan_game_id]
            row_id = arr.find_row_id(data_game, c.csvID_game_id, game_id)
            list_game = arr.fungsi_append(list_game, data_game[row_id])

        print(c.l_listing)
        arr.cetak_tabel(list_game)