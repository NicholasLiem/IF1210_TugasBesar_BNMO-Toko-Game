import argparse
import parseran
import os
import time
import operasi_array as arr

import login
import register
import tambah_game
import ubah_game
import constant as c

data_user = []
data_user_baru = []
data_game = []
data_game_baru = []
data_riwayat = []
data_riwayat_baru = []
data_kepemilikan = []
data_kepemilikan_baru = []

def load():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('nama_folder', help='nama folder tempat data program tersimpan')
    args = argparser.parse_args()
    directory = args.nama_folder
    if os.path.isdir(directory):
        for i in range(4):
            print('Loading' + '.' * i, end='\r')
            time.sleep(0.5)
        print()
        print('\nSelamat datang di antarmuka "Binomo"\n')
        data_game = parseran.csv_to_matrix(directory + '/game.csv')
        data_user = parseran.csv_to_matrix(directory + '/user.csv')
        data_riwayat = parseran.csv_to_matrix(directory + '/riwayat.csv')
        data_kepemilikan = parseran.csv_to_matrix(directory + '/kepemilikan.csv')
        return (True, data_game, data_user, data_riwayat, data_kepemilikan)
    else:
        print(f'Folder "{directory}" tidak ditemukan.')
        return (False, [], [], [], [])

def save(data_game, data_user, data_riwayat, data_kepemilikan):
    directory = input('Masukkan nama folder penyimpanan: ')
    if not os.path.isdir(directory):
        os.mkdir(directory)
    print()
    for i in range(4):
        print('Saving' + '.' * i, end='\r')
        time.sleep(0.5)
    parseran.matrix_to_csv(directory + '/game.csv', data_game)
    parseran.matrix_to_csv(directory + '/user.csv', data_user)
    parseran.matrix_to_csv(directory + '/riwayat.csv', data_riwayat)
    parseran.matrix_to_csv(directory + '/kepemilikan.csv', data_kepemilikan)
    print('\nData telah disimpan pada folder ' + directory + '!')

def exit_program(data_user, data_user_baru, data_game, data_game_baru, data_riwayat, data_riwayat_baru, data_kepemilikan, data_kepemilikan_baru):
    if data_user != data_user_baru or data_game != data_game_baru or data_riwayat != data_riwayat_baru or data_kepemilikan != data_kepemilikan_baru:
        simpan = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)')[0]
        while simpan.lower() != 'y' or simpan.lower() != 'n':
            simpan = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)')[0]
    if simpan.lower() == 'y':
        save(data_game=data_game_baru, data_user=data_user_baru, data_riwayat=data_riwayat_baru, data_kepemilikan=data_kepemilikan_baru)

(sukses, data_game, data_user, data_riwayat, data_kepemilikan) = load()
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
    username = login.login(data_user)
    while not selesai:
        command = input('>>> ')
        if command == 'exit':
            exit_program(data_user, data_user_baru, data_game, data_game_baru, data_riwayat, data_riwayat_baru, data_kepemilikan, data_kepemilikan_baru)
            selesai = True
        elif command == 'register':
            if username != 'admin':
                print(c.error_hanya_admin)
            else:
                data_user_baru = register.register(data_user_baru)
        elif command == 'login':
            username = login.login(data_user_baru)
        elif command == 'tambah_game':
            if username != 'admin':
                print(c.error_hanya_admin)
            else:
                data_game_baru = tambah_game.tambah_game(data_game_baru)
        elif command == 'ubah_game':
            if username != 'admin':
                print(c.error_hanya_admin)
            else:
                data_game_baru = ubah_game.ubah_game(data_game_baru)
            