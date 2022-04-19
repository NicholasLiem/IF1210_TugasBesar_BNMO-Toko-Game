import operasi_array as arr
import constant as c

def register(data_user):
    name = input(c.register_nama)
    while True:
        user_baru=input(c.register_username)
        found = False
        for item in data_user:
            if user_baru == item[c.csvID_user_username] :
                found= True
                break
        if not found:
            break
        else:
            print(f"Username {user_baru} sudah terpakai, silakan menggunakan username lain.")

    password = input(c.register_password)
    role = "user"
    balance= "0"
    id = str(arr.panjang_baris(data_user))
    data_temp = [id,user_baru,name,password,role,balance]

    print(f"Username {user_baru} telah berhasil register ke dalam Binomo")
    
    data_user = arr.fungsi_append(data_user, data_temp)
    return data_user