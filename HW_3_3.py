#задание 3
aa=10
bb=22
cc=5
def my_func(a,b,c):
    flist=[]
    flist.append(a)
    flist.append(b)
    flist.append(c)
    flist.sort()
    flist.pop(0)
    return sum(flist)
print('Результат:', my_func(aa,bb,cc))