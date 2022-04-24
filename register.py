#Penulis Modul: Darren - 16521063
#Judul Modul: Register
#Tanggal: 9 April 2022

import operasi_array as arr
import constant as c

def register(data_user):
    #input nama user
    name = input(c.register_nama)
    user_baru = input(c.register_username)
    password = input(c.register_password)

    #Batas 2
    while arr.found_in_kolom(data_user, c.csvID_user_username, user_baru) or (name == "" or user_baru == "" or password == ""):
        if (name == "" or user_baru == "" or password == ""):
            print("Nama, username, atau password tidak boleh kosong")
        else:
            print(f"Username {user_baru} sudah terpakai, silahkan gunakan username lain.")
        name = input(c.register_nama)
        user_baru = input(c.register_username)
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