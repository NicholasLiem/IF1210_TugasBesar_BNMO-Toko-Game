#Penulis Modul: Darren - 16521063
#Judul Modul: Register
#Tanggal: 9 April 2022

import operasi_array as arr
import constant as c

def register(data_user):
    #input nama user
    name = input(c.register_nama)
    while True:
        #input username
        user_baru = input(c.register_username)
        found = False
        for item in data_user:
            #jika ditemukan username yang sama pada data csv maka akan dicetak pemberitahuan di line 23
            if user_baru == item[c.csvID_user_username] :
                found= True
                break
        if not found:
            break
        else: #found = True
            print(f"Username {user_baru} sudah terpakai, silakan menggunakan username lain.")

    #input password
    password = input(c.register_password)
    #role secara otomatis menjadi user
    role = "user" 
    balance= "0"
    id = str(arr.panjang_baris(data_user))
    data_temp = [id,user_baru,name,password,role,balance]

    print(f"Username {user_baru} telah berhasil register ke dalam Binomo")
    #data_user disimpan sebagai array lokal
    data_user = arr.fungsi_append(data_user, data_temp)
    return data_user