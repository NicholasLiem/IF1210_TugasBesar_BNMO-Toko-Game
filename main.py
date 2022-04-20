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

data_user = []
data_user_baru = []
data_game = []
data_game_baru = []
data_riwayat = []
data_riwayat_baru = []
data_kepemilikan = []
data_kepemilikan_baru = []

(sukses, data_game, data_user, data_riwayat, data_kepemilikan) = load.load()
data_game_baru = arr.copy(data_game)
data_user_baru = arr.copy(data_user)
data_riwayat_baru = arr.copy(data_riwayat)
data_kepemilikan_baru = arr.copy(data_kepemilikan)

selesai = False

if sukses:
    command = input('>>> ')
    while command != 'login':
        print('Maaf, Anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
        command = input('>>> ')
    (username, role) = login.login(data_user)
    while not selesai:
        command = input('>>> ')
        if command == 'register':
            if role != 'admin':
                print(c.error_hanya_admin)
            else:
                data_user_baru = register.register(data_user_baru)

        elif command == 'login':
            username = login.login(data_user_baru)
            
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
        elif command == 'ubah_stok':
            if role != 'admin':
                print(c.error_hanya_admin)
            else:
                data_game_baru = ubah_stok.ubah_stok(data_game_baru)
        elif command == 'list_game':
            list_game.list_game(data_game_baru, data_kepemilikan_baru, username)
        elif command == 'buy_game':
            if role != 'user':
                print(c.error_hanya_user)
            else:
                ...
        elif command == 'list_game_toko':
            ...
        elif command == 'search_my_game':
            if role != 'user':
                print(c.error_hanya_user)
            else:
                search_my_game.search_my_game(data_riwayat_baru, username)
        elif command == 'search_game_at_store':
            find_game.search_game_at_store(data_game_baru)
        elif command == 'topup':
            if role != 'admin':
                print(c.error_hanya_admin)
            else:
                topup.topup(data_user_baru)
        elif command == 'riwayat':
            if role != 'user':
                print(c.error_hanya_admin)
            else:
                riwayat.riwayat(data_riwayat_baru, username)
        elif command == 'help':
            help.help(role)
        elif command == 'save':
            save.save(data_game=data_game_baru, data_user=data_user_baru, data_riwayat=data_riwayat_baru, data_kepemilikan=data_kepemilikan_baru)
        elif command == 'exit':
            exit_program.exit_program(data_user, data_user_baru, data_game, data_game_baru, data_riwayat, data_riwayat_baru, data_kepemilikan, data_kepemilikan_baru)
            selesai = True
            