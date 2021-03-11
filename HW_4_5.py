# урок 4 задание 5
from functools import reduce
items = [x for x in range(1,6) if x % 1==0];
print (items)
print ('Формируем список четных элементов от 100 до 1000 включительно:')
print()
print ("Теперь все элементы перемножаем : ")
mult_all=reduce(lambda x,y: x*y,items)
print(mult_all)



