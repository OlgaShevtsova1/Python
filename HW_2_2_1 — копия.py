# Задача 4
mylist=[0,1,2,3,4,5,6,7,8]
print(mylist)
print()
def ChangeList(mylist) :
    lenlist=len(mylist)
    i=0
    while i<lenlist:
        mlist.insert(i+2,mylist[i])
        mylist.remove(i)
        i+=2
        return mylist
    ChangeList(mylist)
    print(mylist)

