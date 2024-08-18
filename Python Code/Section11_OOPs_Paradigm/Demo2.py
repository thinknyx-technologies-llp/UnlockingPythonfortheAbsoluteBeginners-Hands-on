class Car:
    wheels = 4
    def __init__(self, model):
        self.__model = model
    def get_model(self):
        return self.__model
    def update_model(self, model):
        self.__model = model

obj = Car("Toyota Camry")
print(obj.wheels)
obj.update_model("Honda Civic")
print(obj.get_model())