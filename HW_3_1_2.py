#задание 1 вариант 2
def foo(a,b):
    try:
        return a/b
    except:
        "division by zero"

a=int(input("введите делитель: "))
b=int(input("введите делитель: "))
print("Результат", foo(a, b))