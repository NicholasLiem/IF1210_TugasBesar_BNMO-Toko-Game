#Penulis Modul: Darren - 16521063
#Judul Modul: Login
#Tanggal: 9 April 2022

import constant as c

def login(data_user):
    #user melakukan input username dan password
    username=input(c.login_username)
    password=input(c.login_password)
    #has_logged_in diset sebagai False karena belum terlogin
    has_logged_in = False
    #apabila ditemukan username dan password yang sama di csv dengan yang diinput oleh user maka terdeteksi bahwa login berhasil
    for item in data_user:
        if item[c.csvID_user_username] == username:
            if item[c.csvID_user_password] == password:
                print (f"Halo {item[c.csvID_user_nama]} Selamat datang di Binomo")
                has_logged_in = True
                role = item[c.csvID_user_role]
                return username, role

    #apabila tidak ditemukan username dan password yang sama di csv dengan yang diinput oleh user maka login gagal                  
    if has_logged_in == False:
        print(c.login_invalid)
        return has_logged_in