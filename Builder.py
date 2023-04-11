class boss():
    def __init__(self, name):
        self.name = name

    def get_car_without_backseats(self):
        #config#1
        self.name.get_car()
        self.name.add_model()
        self.name.add_engine()
        self.name.add_tire()

    def get_car_with_backseats(self):
        #config#2
        self.name.get_car()
        self.name.add_model()
        self.name.add_engine()
        self.name.add_tire()
        self.name.add_backseats()

    def get_car(self):
        return self.name.car

class builder():
    # generează clasa car și o predă constructorului engine_builder
    def __init__(self, car=None):
        self.car = car

    def get_car(self):
        self.car = car()


class engine_builder(builder):
    # initializează atributele clasei car
    def add_model(self):
        self.car.model = 'Skoda Rapid 2016'

    def add_engine(self):
        self.car.engine = "1.4 TDI"

    def add_tire(self):
        self.car.tire = 'Continental'
    
    def add_backseats(self):
        self.car.backseats = 'banchete'

class car():
    # aceasta este clasa de bază care trebuie inițializată
    def __init__(self):
        self.model = None
        self.engine = None
        self.tire = None
        self.backseats = None

    def __str__(self):
        if self.backseats:
            return f"Aceasta este mașina model: {self.model}, motor: {self.engine}, anvelope: {self.tire} cu {self.backseats}"
        else:
            return f"Aceasta este mașina model: {self.model}, motor: {self.engine}, anvelope: {self.tire} fără banchete"

car_obj = car()
carBuilder = engine_builder(car_obj)
build_car = boss(carBuilder)
build_car.get_car_without_backseats()
car_built = build_car.get_car()
print(car_built)

car_obj_backseats = car()
carBuilder = engine_builder(car_obj_backseats)
build_car = boss(carBuilder)
build_car.get_car_with_backseats()
car_built = build_car.get_car()
print(car_built)
