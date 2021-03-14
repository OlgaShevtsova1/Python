# урок 5 задание 5
import random
L=[]
f= open("test6.txt","w")
try:
    for i in range(20):
        f.write(str(random.randint(0,100))+"")
finally:
    f.close()
f=open("test6.txt","r")
try:
    fstr=f.readline()
    L=fstr.split()
    Lint=[int(L[i]) for i in range(len(L))]
    print ("Сумма последовательности=", sum(Lint))
finally:
    f.close()