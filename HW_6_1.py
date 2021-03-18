# урок 6 задание 1
import time
class TrafficLight:
    __color="color"

    def running (self,):
     print(f"Запуск")

     self.__color="red"
     print(f"Горит цвет {self.__color}")
     time.sleep(7)

     self.__color="yellow"
     print(f"Горит цвет {self.__color}")
     time.sleep(2)

     self.__color = "green"
     print(f"Горит цвет {self.__color}")
     time.sleep(8)

     while True:
         self.running()

traff_light=TrafficLight()
print(traff_light.running())



