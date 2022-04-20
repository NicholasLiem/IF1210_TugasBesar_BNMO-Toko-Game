import os
import time
import argparse
import parseran

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