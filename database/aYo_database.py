#from csv import reader

"""
    Manages the aYo Database

    To use:
        this must be in your header -> from aYo_database import Database

        Functions to be used outside of this file:
            Check_Login("username here", "password here")
                this will return true if login is ok

            CreateUserProfile("username here", "password here")
                will return false if the username is taken
                will return true if the username is not taken and the database was updated
"""
import os

from .aYo_decode import Decode
from .aYo_encode import Encode

decoder = Decode()
encoder = Encode()

current_path = os.path.dirname(__file__)
un_file_path = os.path.abspath(os.path.join(current_path, "..", "database", "aYo_un_database.csv"))
pw_file_path = os.path.abspath(os.path.join(current_path, "..", "database", "aYo_pw_database.csv"))

def Read_File_Contents(file_name):
    # r tells python to open in read-only mode
    file_object_input  = open(file_name, "r")
    # -> place all of the file in file_contents
    file_contents = file_object_input.read()
    file_object_input.close()
    return file_contents
# end readFileContents

def Get_List(text):
    the_list = []

    lines = text.split( '\n' )

    # removes all empty lines (especially the last one ...)
    lines = [ line for line in lines if line.strip() ]

    for i, line in enumerate( lines ):
        the_list.append(line)

    return the_list

class Database:

    from .aYo_decode import Decode
    from .aYo_encode import Encode

    decoder = Decode()
    encoder = Encode()

    def Check_If_Username_In_Use(self, name):
        user_names = decoder.decode(Read_File_Contents(un_file_path))
        if user_names.find("" + name) > -1:
            return True
        else:
            return False

    def Check_Login(name, password ):
        user_names = decoder.decode(Read_File_Contents(un_file_path))
        the_passwords = decoder.decode(Read_File_Contents(pw_file_path))

        username_list = Get_List(user_names)
        password_list = Get_List(the_passwords)

        check_user = user_names.find(name)

        print(check_user)

        if check_user > -1:
            if password_list[check_user] == password:
                return True
        return False

    def Create_User_Profile(name, password):
        

        user_names = decoder.decode(Read_File_Contents(un_file_path))
        check = False
        if user_names.find("" + name) == -1:
            check = True

        if check == True:
            file_object_output = open(un_file_path,"a")
            file_object_output.write(encoder.encode(name) + "\n")
            file_object_output.close()
            file_object_output = open(pw_file_path, "a")
            file_object_output.write(encoder.encode(password) + "\n")
            file_object_output.close()
        return check
