#Penulis Modul: Moch. Sofyan Firdaus (16521144)
#Judul Modul: Parseran
#Tanggal: 9 April 2022
#Deskripsi: Fungsi ini menangani program sebelum dijalankan, yaitu membaca argument ketika
#           program dijalankan. Argument yang diberikan yaitu berupa nama sebuah folder yang
#           berisi data-data csv yang sudah ditentukan.

import os
import time
import argparse
import parseran

def load():
    # Membuat Argument Parser 
    argparser = argparse.ArgumentParser()
    # Menambahkan argument nama_folder
    argparser.add_argument('nama_folder', help='nama folder tempat data program tersimpan')
    # Menampung argument
    args = argparser.parse_args()
    directory = args.nama_folder
    # Memvalidasi directory 
    if os.path.isdir(directory): # Jika directory merupakan sebuah folder
        for i in range(4):
            print('Loading' + '.' * i, end='\r')
            time.sleep(0.5)
        print()
        print('\nSelamat datang di antarmuka "Binomo"\n')
        # Memindahkan semua data csv ke dalam variabel
        data_game = parseran.csv_to_matrix(directory + '/game.csv')
        data_user = parseran.csv_to_matrix(directory + '/user.csv')
        data_riwayat = parseran.csv_to_matrix(directory + '/riwayat.csv')
        data_kepemilikan = parseran.csv_to_matrix(directory + '/kepemilikan.csv')
        return (True, data_game, data_user, data_riwayat, data_kepemilikan)
        
    else: # Jika directory bukan folder / tidak ada folder directory
        print(f'Folder "{directory}" tidak ditemukan.')
        return (False, [], [], [], [])