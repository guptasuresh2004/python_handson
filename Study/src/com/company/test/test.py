#from car import Car,ElectricCar
import car

print("hello suresh")
abc = ["suresh","kumar",33]
print(abc)

for a in abc:
    print(a)

my_car = car.Car('BMW',7,'2017')
my_car.get_details()


        
        
my_Ecar= car.ElectricCar("Suresh's tesla",5,"2018")
my_Ecar.get_details()
my_Ecar.car_capacity()
        
    