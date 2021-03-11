# Задача 5
Reiting= [7,5,3,3,2] #начало
print()
print("Рейтинг:",Reiting)
r=-1
while r!=0:
    r=int(input("Введите целое число от 0 до 10"))
    Reiting.append(r)
    Reiting.sort ()
    Reiting.reverse()
    print("Рейтинг: ",Reiting)
    print()

