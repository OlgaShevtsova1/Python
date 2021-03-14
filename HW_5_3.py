# урок 5 задание 2_read

f = open("test3.txt","r")
L= []
ZP=[]
try:
    for line in f:
        L.append(line.split())
        ZP.append(line.split())
finally:
    f.close()
#сотрудники
print("Список сотрудников:")
[print(L[i][0]) for i in range(len(L))]
print()

print("Список сотрудников, зарплата которых меньше 30 тыс. руб")
[print (L[i]) for i in range(len(L)) if int(L[i][1])< 30000]

#зарплата
Z=[]
[Z.append(int(ZP[i][1])) for i in range(len(ZP))]
print()
print("Средний доход сотрудников", sum(Z)/(len(Z)+1),"руб/мес")
