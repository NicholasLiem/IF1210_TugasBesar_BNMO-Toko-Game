#Penulis Modul: Moch. Sofyan Firdaus (16521144), Nicholas Liem (16521108)
#Judul Modul: Help
#Tanggal: 9 April 2022

def help(role):
    if role == "admin":
        print("\n")
        print("============ HELP ============")
        print("1. register - Untuk melakukan registrasi user baru")
        print("2. login - Untuk melakukan login ke dalam sistem")
        print("3. register - Untuk menambah akun ke data user")
        print("4. tambah_game - Untuk menambah game yang dijual pada toko")
        print("5. ubah_game - Untuk mengubah data game")
        print("6. ubah_stok - Untuk mengubah stok game")
        print("7. list_game_toko - Untuk melihat list game yang dijual pada toko")
        print("8. search_game_at_store - Untuk mencari game pada toko")
        print("9. topup - Untuk melakukan topup saldo")
        print("10. save - Untuk melakukan penyimpanan data")
        print("11. exit - Untuk keluar dari program")
        print("\n")

    elif role == "user":
        print("\n")
        print("============ HELP ============")
        print("1. login - Untuk melakukan login ke dalam sistem")
        print("2. list_game_toko - Untuk melihat list game yang dijual pada toko")
        print("3. buy_game - Untuk membeli game")
        print("4. list_game - Untuk melihat daftar game yang dimiliki pengguna")
        print("5. seach_my_game - Untuk melihat daftar game pengguna berdasarkan ID dan tahun rilis")
        print("6. search_game_at_store - Untuk mencari game pada toko")
        print("7. riwayat - Untuk melihat riwayat pembelian game")
        print("8. save - Untuk melakukan penyimpanan data")
        print("9. exit - Untuk keluar dari program")
        print("\n")
        
    else:
        print("\n")
        print("============ HELP ============")
        print("1. login - Untuk melakukan login ke dalam sistem")
        print("2. help - Untuk melihat perintah yang bisa dilakukan")
        print("\n")