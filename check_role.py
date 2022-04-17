import parseran
import operasi_array as arr
import constant as c

def check_role(username,id):
    array = parseran.csv_to_matrix("Data/user.csv")
    role = arr.find_value_in_same_row(array,c.csvID_user_id,id,c.csvID_user_role)
    if username == "" and id != "":
        if role != False:
            return role
        else:
            return role
    elif username != "" and id == "":
        if role != False:
            return role
        else:
            return role
    else:
        return role