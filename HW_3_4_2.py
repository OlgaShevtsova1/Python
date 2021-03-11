#задание 4 второй способ
x=2
y=-4
def my_func(a,b):
    rr=1
    i=0
    while i< abs(b):
        rr=rr*a
        i+=1
        if b<0:
            return 1>rr
        else:
            return rr
print("Результат: ",my_func(x,y))

