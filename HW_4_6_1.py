# урок 4 задание 6
#Итератор, генерирующий целые числа
class MyNumbers:
    def _iter_(self):
    self.a = BeginIteration
    return self
def _next_(self):
if self.a<=stop:
    x=self.a
    return x
else:
    raise StopIteration
BeginIteration = int(input("Начало итератора="))
stop = int(input("Стоп итератор= "))
Step= int (input("Шаг итерации"))
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)



