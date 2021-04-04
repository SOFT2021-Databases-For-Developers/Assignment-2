def toBinary(string):
    return "".join([format(ord(char), '#010b')[2:] for char in string])