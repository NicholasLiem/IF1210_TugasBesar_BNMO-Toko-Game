import argparse
import parseran
import os
import time
import operasi_array as arr

data_user = []
data_user_baru = []
data_game = []
data_game_baru = []
data_riwayat = []
data_riwayat_baru = []
data_kepemilikan = []
data_kepemilikan_baru = []

def load(directory):
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

def exit():
    ...

(sukses, data_game, data_user, data_riwayat, data_kepemilikan) = load('Data')

if sukses:
    save(data_game=data_game, data_user=data_user, data_riwayat=data_riwayat, data_kepemilikan=data_kepemilikan)