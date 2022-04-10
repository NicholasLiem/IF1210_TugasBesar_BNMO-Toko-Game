import operasi_array as arr
import parseran
import constant as c

dir = "Data/kepemilikan.csv"
data_kepemilikan = parseran.csv_to_matrix(dir)
data_game = parseran.csv_to_matrix("Data/game.csv")

def list_game():
    user = input("Login session user: ")
    #usernya harusnya diambil dari login sessionnya. tapi strukturnya harusnya udah jadi.
    #Login session, user.
    if not(arr.found_in_kolom(data_kepemilikan, c.csvID_kepemilikan_user_id, user)):
        print(c.l_notFound)
    else:
        list_game = []
        game_id_kepemilikan_user = arr.all_valid_row(data_kepemilikan, c.csvID_kepemilikan_user_id, user)
        for item in game_id_kepemilikan_user:
            list_game = arr.fungsi_append(list_game,arr.all_valid_row(data_game, c.csvID_id, item[c.csvID_kepemilikan_game_id]))
        print(c.l_listing)
        for item in list_game:
            print(item)

list_game()