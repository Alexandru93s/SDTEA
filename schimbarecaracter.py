# functie recursiva care inlocuieste un caracter dintr-un sir cu altul

st = "asdfghddxohidddpd"
ch1 = "d"
ch2 = "z"

def replaceChar(st, charToFind, charForReplace):
  if len(st) > 0:
    if st[0] == charToFind:
      return charForReplace + replaceChar(st[1:], charToFind, charForReplace)
    else: return st[0] + replaceChar(st[1:], charToFind, charForReplace)
  else: return ""

print(replaceChar(st, ch1, ch2))