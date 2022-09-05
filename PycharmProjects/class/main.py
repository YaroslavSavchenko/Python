class House():
    """Описание дома"""
    def __init__(self,street,number):
        """Свойства дома"""
        self.street = street
        self.number = number
        self.age = 0
    def build(self):
        """Строит дом"""
        print("Дом на улице " + self.street + " под номером " + str(self.number) + " Построен.")
    def age_of_house (self,year):
        """Возраст дома"""
        self.age += year

"""
House1 = House("Соборна",32)
House2 = House("Соборна",24)
# print(House1.street)
# House1.build()
House1.age_of_house(5)
print(House1.age)
"""

class ProspectHouse(House):
    """Дома на проспекте"""
    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect

PrHouse = ProspectHouse("Черновола", 12)
print(PrHouse.prospect)
