class Vehicle:
    def start(self, fule_type):
        return f"The vehicle's engine has started with {fule_type}."
    
class Car(Vehicle):
    def start(self, fuel_type, car_model):
        base_message = super().start(fuel_type)
        return f"{base_message} This is a {car_model} car."
    
class SportsCar(Car):
    def start(self, fule_tupe, car_model, top_speed):
        base_message = super().start(fule_tupe, car_model)
        return f"{base_message} It has a top speed of {top_speed} km/h."
    
class Truck(Vehicle):
    def start(self, fuel_type, ignition_type):
        return f"The Truck's engine has started with {fuel_type} and {ignition_type} ignition."
    

obj_vehicle = Vehicle()
obj_car = Car()
obj_sports_car = SportsCar()
obj_truck = Truck()

print(obj_vehicle.start('petrol'))
print(obj_car.start('diesel','Sedan'))
print(obj_sports_car.start('premium','Convertible', 300))
print(obj_truck.start('diesel', 'electric'))