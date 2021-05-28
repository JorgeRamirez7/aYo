

class Encode:
    def encode(self, aString):

        string_list = list(aString)

        for index, item in enumerate(string_list):
            #lowercase
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
            #Capitals
            if item == 'A':
                string_list[index] = 'G'
            if item == 'B':
                string_list[index] = 'H'
            if item == 'C':
                string_list[index] = 'X'
            if item == 'D':
                string_list[index] = 'C'
            if item == 'E':
                string_list[index] = 'T'
            if item == 'F':
                string_list[index] = 'V'
            if item == 'G':
                string_list[index] = 'U'
            if item == 'H':
                string_list[index] = 'D'
            if item == 'I':
                string_list[index] = 'A'
            if item == 'J':
                string_list[index] = 'W'
            if item == 'K':
                string_list[index] = 'Z'
            if item == 'L':
                string_list[index] = 'M'
            if item == 'M':
                string_list[index] = 'I'
            if item == 'N':
                string_list[index] = 'K'
            if item == 'O':
                string_list[index] = 'B'
            if item == 'P':
                string_list[index] = 'E'
            if item == 'Q':
                string_list[index] = 'N'
            if item == 'R':
                string_list[index] = 'F'
            if item == 'S':
                string_list[index] = 'J'
            if item == 'T':
                string_list[index] = 'L'
            if item == 'U':
                string_list[index] = 'S'
            if item == 'V':
                string_list[index] = 'Y'
            if item == 'W':
                string_list[index] = 'Q'
            if item == 'X':
                string_list[index] = 'P'
            if item == 'Y':
                string_list[index] = 'O'
            if item == 'Z':
                string_list[index] = 'R'
            #numbers
            if item == '0':
                string_list[index] = '9'
            if item == '1':
                string_list[index] = '8'
            if item == '2':
                string_list[index] = '7'
            if item == '3':
                string_list[index] = '6'
            if item == '4':
                string_list[index] = '5'
            if item == '5':
                string_list[index] = '4'
            if item == '6':
                string_list[index] = '3'
            if item == '7':
                string_list[index] = '2'
            if item == '8':
                string_list[index] = '1'
            if item == '9':
                string_list[index] = '0'
            #special characters
            if item == '!':
                string_list[index] = ')'
            if item == '@':
                string_list[index] = '('
            if item == '#':
                string_list[index] = '*'
            if item == '$':
                string_list[index] = '&'
            if item == '%':
                string_list[index] = '^'
            if item == '^':
                string_list[index] = '%'
            if item == '&':
                string_list[index] = '$'
            if item == '*':
                string_list[index] = '#'
            if item == '(':
                string_list[index] = '@'
            if item == ')':
                string_list[index] = '!'
        new_string = "".join(string_list)
        return new_string
