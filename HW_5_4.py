# урок 5 задание 4
trlate= ["Один","Два","Три","Четыре","Пять"]
f = open("test5.txt","r")
L=[]
try:
    for line in f:
        L.append(line.split())
finally:
    f.close()
f=open("test5tr.txt","w")
try:
    for i in range(len(L)):
        L[i].remove(L[i][0])
        L[i].insert([0][0],trlate[i])
        f.write(str(L[i])+"/n")
finally:
    f.close()
print("Готово!")
print("Результат см. в файле test5tr.txt")