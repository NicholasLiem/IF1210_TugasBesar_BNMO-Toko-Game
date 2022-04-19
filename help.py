import return_role as rr

def help(data_user,username):
    role = rr.return_role(data_user, username)
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
