# урок 4 задание 6.2
#Итератор, повторяющий заданный список
from itertools import cycle
lst = [2,5,3,6,7,8,9]
count=0
for item in cycle(lst):
    if count > len(lst)-1:
        break
        print(item)
        count +=1




