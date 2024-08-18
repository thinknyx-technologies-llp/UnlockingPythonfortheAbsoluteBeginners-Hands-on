class Car:
    wheels = 4
    def __init__(self,model):
        self.model = model
    def wheel(self):
        print(f"The number of wheels on my car is: {self.wheels}")

object = Car("Toyota Camry")
print(object.wheel())