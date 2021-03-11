# урок 4 задание 7
def fact(n):
    a = 1
    for i in range (1,n+1):
        a *= i
        yield a
N= int(input("Введите число N:"))
k=1
for el in fact(N):
    print("Число N=",k,"факториал N= ", el)
    k+=1




