# The following file has been created by Heather Willis
# This file contains three functions, one of which converts
# a string to chars and chars to a string,
# another converts chars to ASCII and ASCII to chars,
# the last one converts binary to ASCII and ASCII to binary.
# Please read the following comments to under this line by line

# create a function that converts a string in characters and characters into a string
def charAndStr(string, chars):
    strList = list(string)  # create a list from a string this will break down the chars in the string
    charList = "".join(chars)  # create a string from given chars
    return strList, charList  # return both values (so they can be used)


# create a function that will convert chars into ASCII values and vice versa
def charAndASCII(chars, ASCIINums):
    charToASCII = [ord(chars) for chars in list(chars)]  # turn the chars into ASCII values
    ASCIIToChar = list(''.join(chr(i) for i in ASCIINums))  # 1st create a string of the ASCII values then convert that into a list
    return charToASCII, ASCIIToChar  # return the ASCII and char values


# create a function that will convert binary to ASCII and vice versa
def BinAndASCII(Bin, ASCIINums):
    listOfASCII = []  # create an empty list
    for i in ASCIINums:  # loop through the ASCII values
        if i < 127:  # check if it is in range
            listOfASCII.append(int("{0:8b}".format(i)))  # append to empty list

    listOfBin = []  # create another empty list
    for i in Bin:  # loop through the binary values
        if i > 127:  # check if it is in range
            listOfBin.append(int(str(i), 2))  # append to empty list
    return listOfASCII, listOfBin  # return these values


# create main
if __name__ == '__main__':
    string = "Heather Willis"  # string defined here
    chars = 'H', 'e', 'a', 't', 'h', 'e', 'r', ' ', 'W', 'i', 'l', 'l', 'i', 's'  # characters defined here
    ASCIINums = 72, 101, 97, 116, 104, 101, 114, 32, 87, 105, 108, 108, 105, 115  # ASCII values defined here
    Bin = 1001000, 1100101, 1100001, 1110100, 1101000, 1100101, 1110010, 100000, 1010111, 1101001, 1101100, 1101100, 1101001, 1110011  # binary values defined here only one with 1st letter captial because bin() exists

    # here all the values are being printed and functions being called to be used
    print(charAndStr(string, chars))
    print(charAndASCII(chars, ASCIINums))
    print(BinAndASCII(Bin, ASCIINums))