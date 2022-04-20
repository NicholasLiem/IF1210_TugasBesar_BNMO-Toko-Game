#Penulis Modul: Darren (16521063)
#Judul Modul: Find Game
#Tanggal: 20 April 2022

import constant as c

def login(data_user):
    username=input(c.login_username)
    password=input(c.login_password)
    has_logged_in = False
    for item in data_user:
        if item[c.csvID_user_username] == username:
            if item[c.csvID_user_password] == password:
                print (f"Halo {item[c.csvID_user_nama]} Selamat datang di Binomo")
                has_logged_in = True
                role = item[c.csvID_user_role]
                return username, role
                      
    if has_logged_in == False:
        print(c.login_invalid)
        return has_logged_in