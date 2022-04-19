import operasi_array as arr
import parseran
import constant as c

# dir = "Data/user.csv"
# data_user = parseran.csv_to_matrix(dir)

def help(data_user,username):
    row_id = arr.find_row_id(data_user,c.csvID_user_username,username)
    role = data_user[row_id][c.csvID_user_role]
    if role == "admin":
        print("============ HELP ============")
        print("1. register - Untuk melakukan registrasi user baru")
        print("2. login - Untuk melakukan login ke dalam sistem")
        print("3. tambah_game - Untuk menambah game yang dijual pada toko")
        print("4. list_game_toko - Untuk melihat list game yang dijual pada toko")
    else:
        print("============ HELP ============")
        print("1. login - Untuk melakukan login ke dalam sistem")
        print("2. list_game_toko - Untuk melihat list game yang dijual pada toko")

