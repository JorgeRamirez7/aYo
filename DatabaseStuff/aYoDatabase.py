#from csv import reader

def encode(aString):
    return aString

def decode(aString):
    return aString


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
