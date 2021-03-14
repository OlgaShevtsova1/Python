# урок 5 задание 1_write
#Пишет в файл example.txt
f = open('example.txt','w')

st = True
try:
    while st:
        st = input('Введите строку:')
        f.write(st+'\n')
finally:
        f.close()





