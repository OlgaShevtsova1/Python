# урок 5 задание 2_read
#читает файл  test.txt
f = open('test.txt','r')
string=0
try:
    for line in f:
        print(line,"word in string=",len((line.split())))
        print()
        string+=1
finally:
    print("Всего strings=",string)
    f.close()

