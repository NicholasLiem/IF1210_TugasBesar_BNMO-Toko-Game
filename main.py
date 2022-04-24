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
import buy_game
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

status = ("", "", False)

(sukses, data_game, data_user, data_riwayat, data_kepemilikan) = load.load()
data_game_baru = arr.copy(data_game)
data_user_baru = arr.copy(data_user)
data_riwayat_baru = arr.copy(data_riwayat)
data_kepemilikan_baru = arr.copy(data_kepemilikan)

selesai = False
if sukses:
    command = input('>>> ')
    while command != 'login' and command != 'help':
        print(c.error_belum_login)
        command = input('>>> ')
    if command == 'login':
        status = login.login(data_user_baru,status)
    else:
        help.help('')
    while not selesai:
        command = input('>>> ')
        if command == 'register':
            if status[1] != 'admin':
                print(c.error_hanya_admin)
            else:
                data_user_baru = register.register(data_user_baru)
        elif command == 'login':
            status = login.login(data_user_baru,status)
            
        elif command == 'tambah_game':
            if status[1] != 'admin':
                print(c.error_hanya_admin)
            else:
                data_game_baru = tambah_game.tambah_game(data_game_baru)
        elif command == 'ubah_game':
            if status[1] != 'admin':
                print(c.error_hanya_admin)
            else:
                data_game_baru = ubah_game.ubah_game(data_game_baru)
        elif command == 'ubah_stok':
            if status[1] != 'admin':
                print(c.error_hanya_admin)
            else:
                data_game_baru = ubah_stok.ubah_stok(data_game_baru)
        elif command == 'list_game':
            list_game.list_game(data_game_baru, data_kepemilikan_baru, status[0])
        elif command == 'buy_game':
            if status[1] != 'user':
                print(c.error_hanya_user)
            else:
                data_user_baru, data_game_baru, data_riwayat_baru, data_kepemilikan_baru = buy_game.buy_game(data_user_baru, data_game_baru, data_riwayat_baru, data_kepemilikan_baru, status[0])
        elif command == 'list_game_toko':
            list_game_toko.list_game_toko(data_game_baru)
        elif command == 'search_my_game':
            if status[1] != 'user':
                print(c.error_hanya_user)
            else:
                search_my_game.search_my_game(data_kepemilikan_baru, data_game_baru, status[0])
        elif command == 'search_game_at_store':
            find_game.search_game_at_store(data_game_baru)
        elif command == 'topup':
            if status[1] != 'admin':
                print(c.error_hanya_admin)
            else:
                data_user_baru = topup.topup(data_user_baru)
        elif command == 'riwayat':
            if status[1] != 'user':
                print(c.error_hanya_admin)
            else:
                riwayat.riwayat(data_riwayat_baru, status[0])
        elif command == 'help':
            help.help(status[1])
        elif command == 'save':
            save.save(data_game=data_game_baru, data_user=data_user_baru, data_riwayat=data_riwayat_baru, data_kepemilikan=data_kepemilikan_baru)
        elif command == 'exit':
            exit_program.exit_program(data_user, data_user_baru, data_game, data_game_baru, data_riwayat, data_riwayat_baru, data_kepemilikan, data_kepemilikan_baru)
            selesai = True 
        else:
            print(f"Tidak ada perintah {command}!")