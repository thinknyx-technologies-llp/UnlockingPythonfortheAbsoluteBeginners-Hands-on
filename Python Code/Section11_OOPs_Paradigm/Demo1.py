class Vehicle:
    def __init__(self):
        self.engine = True
    def get_engine(self):
        return "Every vehicle has an engine"
    
class Car(Vehicle):
    def __init__(self,wheels):
        super().__init__()
        self.wheels = wheels

    def get_wheels(self):
        return f"Car object has {self.wheels} wheels"
obj_vehicle = Vehicle()
obj_car = Car(4)
print(obj_car.engine)
print(obj_car.get_engine())