#Penulis Modul: Nicholas Liem - 16521108
#Judul Modul: Riwayat
#Tanggal: 19 April 2022

import operasi_array as arr
import constant as c

def riwayat(data_riwayat, username):

    if not(arr.found_in_kolom(data_riwayat, c.csvID_riwayat_username,username)):
        print(c.r_notFound)

    else:

        list_riwayat = arr.all_valid_row(data_riwayat, c.csvID_riwayat_username, username)
        #Fungsi delete_column mengembalikan array tanpa kolom yang di minta.
        riwayat_tanpa_id = arr.delete_column(list_riwayat, c.csvID_riwayat_username)
        
        print(c.r_listing)
        arr.cetak_tabel(riwayat_tanpa_id)