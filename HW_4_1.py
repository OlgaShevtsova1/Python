# урок 4 задание 1
def zplata(x,y,z):
    return x*y+z

print('Для расчета зарплаты сотрудника введите:')
x=int(input("Время, ч/месяц=\t"))
y= int(input("Ставка,руб/ч=\t\t"))
z=int(input("Премия, руб=\t\t"))

print('Зарплата Сотрудника за месяц=', zplata(x,y,z),"руб")

