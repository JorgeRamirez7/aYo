#from csv import reader

def encode(aString):

    string_list = list(aString)

    for index, item in enumerate(string_list):
        if item == 'a':
            string_list[index] = 'g'
        if item == 'b':
            string_list[index] = 'h'
        if item == 'c':
            string_list[index] = 'x'
        if item == 'd':
            string_list[index] = 'c'
        if item == 'e':
            string_list[index] = 't'
        if item == 'f':
            string_list[index] = 'v'
        if item == 'g':
            string_list[index] = 'u'
        if item == 'h':
            string_list[index] = 'd'
        if item == 'i':
            string_list[index] = 'a'
        if item == 'j':
            string_list[index] = 'w'
        if item == 'k':
            string_list[index] = 'z'
        if item == 'l':
            string_list[index] = 'm'
        if item == 'm':
            string_list[index] = 'i'
        if item == 'n':
            string_list[index] = 'k'
        if item == 'o':
            string_list[index] = 'b'
        if item == 'p':
            string_list[index] = 'e'
        if item == 'q':
            string_list[index] = 'n'
        if item == 'r':
            string_list[index] = 'f'
        if item == 's':
            string_list[index] = 'j'
        if item == 't':
            string_list[index] = 'l'
        if item == 'u':
            string_list[index] = 's'
        if item == 'v':
            string_list[index] = 'y'
        if item == 'w':
            string_list[index] = 'q'
        if item == 'x':
            string_list[index] = 'p'
        if item == 'y':
            string_list[index] = 'o'
        if item == 'z':
            string_list[index] = 'r'

    new_string = "".join(string_list)
    return new_string

def decode(aString):

    string_list = list(aString)

    for index, item in enumerate(string_list):
        if item == 'g':
            string_list[index] = 'a'
        if item == 'h':
            string_list[index] = 'b'
        if item == 'x':
            string_list[index] = 'c'
        if item == 'c':
            string_list[index] = 'd'
        if item == 't':
            string_list[index] = 'e'
        if item == 'v':
            string_list[index] = 'f'
        if item == 'u':
            string_list[index] = 'g'
        if item == 'd':
            string_list[index] = 'h'
        if item == 'a':
            string_list[index] = 'i'
        if item == 'w':
            string_list[index] = 'j'
        if item == 'z':
            string_list[index] = 'k'
        if item == 'm':
            string_list[index] = 'l'
        if item == 'i':
            string_list[index] = 'm'
        if item == 'k':
            string_list[index] = 'n'
        if item == 'b':
            string_list[index] = 'o'
        if item == 'e':
            string_list[index] = 'p'
        if item == 'n':
            string_list[index] = 'q'
        if item == 'f':
            string_list[index] = 'r'
        if item == 'j':
            string_list[index] = 's'
        if item == 'l':
            string_list[index] = 't'
        if item == 's':
            string_list[index] = 'u'
        if item == 'y':
            string_list[index] = 'v'
        if item == 'q':
            string_list[index] = 'w'
        if item == 'p':
            string_list[index] = 'x'
        if item == 'o':
            string_list[index] = 'y'
        if item == 'r':
            string_list[index] = 'z'

    new_string = "".join(string_list)
    return new_string


def ReadFileContents(fileName):
    # r tells python to open in read-only mode
    fileObjectInput  = open(fileName, "r")
    # -> place all of the file in file_contents
    fileContents = fileObjectInput.read()
    fileObjectInput.close()
    return fileContents
# end readFileContents

def getList(text):
    theList = []

    lines = text.split( '\n' )

    # removes all empty lines (especially the last one ...)
    lines = [ line for line in lines if line.strip() ]

    for i, line in enumerate( lines ):
        theList.append(line)

    return theList

class DataBase:

    def CheckIfUsernameInUse(self, name):
        userNames = ReadFileContents("SampleDatabase.csv")
        if userNames.find("" + name) > -1:
            return True
        else:
            return False

    def CheckLogIn( self, name, password ):
        userNames = ReadFileContents("SampleDatabase.csv")
        thePasswords = ReadFileContents("passwords.csv")

        username_list = getList(userNames)
        password_list = getList(thePasswords)

        print (encode("aaaaaab"))
        #print (username_list)
        checkUser = userNames.find(name)

        if checkUser > -1:
            if password_list[checkUser] == password:
                return True
        return False

    def AddUser(self, new_name, new_password):

        fileObjectOutput = open("SampleDatabase.csv","a")

        fileObjectOutput.write(new_name + "\n")
        fileObjectOutput.close()

        fileObjectOutput = open("passwords.csv", "a")

        fileObjectOutput.write(new_password + "\n")
        fileObjectOutput.close()

    def CreateUserProfile(self, name, password):
        userNames = ReadFileContents("SampleDatabase.csv")
        check = False
        if userNames.find("" + name) == -1:
            check = True

        if check == True:
            fileObjectOutput = open("SampleDatabase.csv","a")
            fileObjectOutput.write(name + "\n")
            fileObjectOutput.close()
            fileObjectOutput = open("passwords.csv", "a")
            fileObjectOutput.write(password + "\n")
            fileObjectOutput.close()
        return check
