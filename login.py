#Penulis Modul: Darren - 16521063
#Judul Modul: Login
#Tanggal: 9 April 2022

import constant as c
import operasi_array as arr

def login(data_user, datatemp):
    #user melakukan input username dan password
    username=input(c.login_username)
    password=input(c.login_password)
    #has_logged_in diset sebagai False karena belum terlogin
    has_logged_in = False
    #apabila ditemukan username dan password yang sama di csv dengan yang diinput oleh user maka terdeteksi bahwa login berhasil
    
    user_valid = arr.found_in_kolom(data_user, c.csvID_user_username, username)
    if user_valid:
        row_user = arr.find_row_id(data_user, c.csvID_user_username, username)
        password_user = data_user[row_user][c.csvID_user_password]

        if password != password_user:
            print(c.login_invalid)
            return(datatemp)
        else:
            print (f"Halo {data_user[row_user][c.csvID_user_nama]}! Selamat datang di Binomo")
            role = data_user[row_user][c.csvID_user_role]
            has_logged_in = True
            return (username, role, has_logged_in)
    else:
        print(c.login_invalid)
        return(datatemp)