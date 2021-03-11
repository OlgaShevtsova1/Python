# урок 4 задание 4
a=[2,2,2,7,23,1,44,44,3,2,10,7,4,11]
b=[a[x] for x in range(len(a))];
print(b)
b=[a[x] for x in range(len(a)) if a.count(a[x])==1];
print(b,a)



