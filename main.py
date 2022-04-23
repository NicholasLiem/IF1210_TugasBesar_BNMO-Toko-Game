#Penulis Modul: Moch. Sofyan Firdaus (16521144)
#Judul Modul: Main
#Tanggal: 19 April 2022

import operasi_array as arr
import login
import register
import tambah_game
import ubah_game
import ubah_stok
import list_game_toko
# import buy_game
import list_game
import search_my_game
import find_game
import topup
import riwayat
import help
import load
import save
import exit_program
import constant as c

(sukses, data_game, data_user, data_riwayat, data_kepemilikan) = load.load()
data_game_baru = arr.copy(data_game)
data_user_baru = arr.copy(data_user)
data_riwayat_baru = arr.copy(data_riwayat)
data_kepemilikan_baru = arr.copy(data_kepemilikan)

selesai = False

if sukses:
    command = input('>>> ')
    while command != 'login' or command != 'help':
        print('Maaf, Anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
        command = input('>>> ')
    if command == 'login':
        (username, role) = login.login(data_user)
    else:
        help.help('')
    while not selesai:
        command = input('>>> ')
        if command == 'register':
            if role != 'admin':
                print(c.error_hanya_admin)
            else:
                data_user_baru = register.register(data_user_baru)

        elif command == 'login':
            (username, role) = login.login(data_user_baru)
            
        elif command == 'tambah_game':
            if role != 'admin':
                print(c.error_hanya_admin)
            else:
                data_game_baru = tambah_game.tambah_game(data_game_baru)

        elif command == 'ubah_game':
            if role != 'admin':
                print(c.error_hanya_admin)
            else:
                data_game_baru = ubah_game.ubah_game(data_game_baru)
