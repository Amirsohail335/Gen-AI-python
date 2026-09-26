class Chai:
    def __init__(self, sweetness,milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

    
    def sip(self):
        print("Sipping chai")

    
    def add_sugar(self,amount):
        print("amount of suger added")


my_tea = Chai(sweetness=4, milk_level=5)

my_tea.add_sugar(7)