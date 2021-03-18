# урок 6 задание 4
class Car:
    speed="speed"
    color= "color"
    name= "name"
    is_police:bool
    def __init__(self,go,stop,turn):
        self._go=go
        print(f"Поехали")
        self._stop=stop
        print(f"Остановилась")
        self.turn=turn
        print (f("Повернула"))
    def show_speed(self):
        print(f"Текущая скорость автомобиля")
class TownCar(Car):
    speed = 45
    color = "Red"
    name = "Ford"
    is_police: False
    def show_speed(self):
        if self.speed>60:
    print (f"Превышение скорости")
class SportCar(Car):
    speed = 100
    color = "yellow"
    name = "BJW"
    is_police: False
class WorkCar(Car):
    speed = 30
    color = "Green"
    name = "TW"
    is_police: False
            def show_speed(self):
                if self.speed > 40:
                    print("Превышение скорости")
class PoliceCar(Car):
    speed = 100
    color = "Black"
    name = "Pol"
    is_police: True

tc=TownCar()
pc=PoliceCar()
sc=SportCar()
wc=WorkCar()

print(tc)
print(pc)
print(sc)
print(wc)
