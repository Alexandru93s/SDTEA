#def remove_odd(l):
#    for i in l[:]:
#        if i % 2 != 0:
#            l.remove(i)
#    return l

#print(remove_odd([1,2,3,4,5,6,7]))

lst = [1,2,3,4,5,6]
newList = [el for el in lst if el%2==0]
print(newList)