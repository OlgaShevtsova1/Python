# Задача 2
print("Введите элементы списка, целые числа 10 шт.")
nn=0
mylist=[]
while nn<10:
    nn=int(input())
    mylist.append(nn)
    nn+=1
print(mylist)
print()
def ChangeList(mlist):
    lenlist = len(mylist)
    i = 0
    while i < lenlist:
        mlist.insert(i+2,mylist(i))
        mlist.remove(mylist(i))
        i+=2
    return mlist
ChangeList(mylist)
print(mylist)


