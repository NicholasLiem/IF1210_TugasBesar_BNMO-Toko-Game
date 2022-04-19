import operasi_array as arr
import constant as c

def return_role(data_user, username):
    row_id = arr.find_row_id(data_user, c.csvID_user_username, username)
    role = data_user[row_id][c.csvID_user_role]
    return role