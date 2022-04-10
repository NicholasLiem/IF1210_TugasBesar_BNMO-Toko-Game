import find_game as fg
import parseran
import constant as c

dir = "Data/riwayat.csv"
data_riwayat = parseran.csv_to_matrix(dir)

def list_game():
    user = input("Login session user: ")
    #Login session, user.
    if not(fg.found_in_kolom(data_riwayat, c.csvID_riwayat_user_id,user)):
        print(c.l_notFound)
    else:
        list_game = fg.all_valid_row(data_riwayat, c.csvID_riwayat_user_id, user)
        for item in list_game:
            print(item)

list_game()