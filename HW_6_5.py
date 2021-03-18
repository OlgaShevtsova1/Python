# урок 6 задание 5
class Stationery:
    title=None
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    title = "Pen"
    def draw(self):
     print(self.title)
class Pencil(Stationery):
    title = "Pencil"
    def draw(self):
     print(self.title)
class Handle(Stationery):
    title = "Handle"
    def draw(self):
     print(self.title)
pen=Pen()
penc=Pencil()
hen=Handle()
st=Stationery()
print(st.draw())
print(pen.draw())
print(penc.draw())
print(hen.draw())
