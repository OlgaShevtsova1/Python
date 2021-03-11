#задание 1
def foo(a,b):
    return a/b
a=int(input("введите делитель: "))
b=int(input("введите делитель: "))
#print ("Результат",foo(a,b))
if b==0:
    print ("Ошибка")
    b=b+1
else:
    print("Результат", foo(a, b))