class Cars():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def move(self):
        print('The Cars can move at high speed.')

class EVs(Cars):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
    
    def selfdriving(self):
        print('EVs can drive autonomously')

toyota = Cars("Toyota", "Hilux", "2023")
bmw = Cars("BMW", "M4", "2024")
tesla = EVs("Tesla", "Cybertaxi", "2025")

tesla.selfdriving() # Output: EVs can drive autonomously
print(tesla.year) # Output: 2025
tesla.move() # Output: The Cars can move at high speed.