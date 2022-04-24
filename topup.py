#Penulis Modul: Nicholas Liem - 16521108
#Judul Modul: Top-up
#Tanggal: 10 April 2022

import operasi_array as arr
import constant as c

def topup(data_user):
    username = input(c.t_username)
    saldo_topup = int(input(c.t_saldo))

    if not arr.found_in_kolom(data_user,c.csvID_user_username,username):
        print(f"Username '{username}' tidak ditemukan.")

    else:
        if saldo_topup != "":
            row_id = arr.find_row_id(data_user,c.csvID_user_username,username)
            nama = data_user[row_id][c.csvID_user_nama]
            saldo_data = int(data_user[row_id][c.csvID_user_saldo])
            new_saldo = saldo_topup + saldo_data

            #Ketika jumlah saldo yang diinput dan yang ada hasilnya negatif, maka tidak bisa diproses
            if new_saldo < 0:
                print(c.t_invalid)
                
            else: #Username ada dan saldo hasil positif
                temp = arr.copy(data_user[row_id])
                temp[c.csvID_user_saldo] = str(new_saldo)
                data_user[row_id] = temp
                print(f"Top up berhasil. Saldo {nama} berubah menjadi {new_saldo}.")
        else:
            print("Saldo topup tidak boleh kosong!")
    return data_user