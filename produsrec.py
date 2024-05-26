def produs(p):
    if p == 1: 
        return 1
    else:
        return p * produs(p-1)
    
print(produs(3))
