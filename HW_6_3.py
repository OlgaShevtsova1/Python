# урок 6 задание 3

class Worker:
    name= "name"
    surname= "surname"
    position= "position"
    _income= {
        "wage":"wage",
        "bonus":"bonus"
    }
class Position(Worker):
    def __init__(self,name:str,surname:str,wage:float,bonus:float):
        self.name=name
        self.surname=surname
        self._income['wage']= wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        print(self.name + self.surname)
    def get_total_income (self):
        print(self._income['wage'] + self._income['bonus'])

p=Position(name="NO",surname="Name",wage=12,bonus=5)
print(p.get_full_name())
print(p.get_total_income())
