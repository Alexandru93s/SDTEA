#schimbare caracter recursive
""" st = "addddssa"
ch1 = "d"
ch2 = "x"

def replace_char(st, charToFind,charToReplace):
    if len(st) > 0:
        if st[0] == charToFind:
            return charToReplace + replace_char(st[1:], charToFind, charToReplace)
        else:
            return st[0] + replace_char(st[1:], charToFind, charToReplace)
    else:
        return ""
    
print(replace_char(st,ch1,ch2))
         """
#sterge impare
""" list = [1,2,3,4,5,6,7,8,9]

newlist = [el for el in list if el%2==0]
print(newlist) """

#sumanrnat
""" def suma_nrnat(n):
    if n == 0:
        return n
    else:
        return n + suma_nrnat(n-1)
print(suma_nrnat(5)) """

#produsnrnat
""" def produs_nrnat(n):
    if n == 1:
        return n
    else:
        return n * produs_nrnat(n-1)

print(produs_nrnat(4)) """
#