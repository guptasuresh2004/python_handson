from battery import Battery
class Car():
    def __init__(self,name,price,model_year="2017"):
        self.name= name
        self.price =price
        self.model_year=model_year 
        
    def get_details(self):
        print("car name---"+self.name.title())
        print("car price---"+str(self.price)+"Lakhs")
        print("car model year---"+self.model_year)

class ElectricCar(Car):
    def __init__(self,name,price,model_year):
        super().__init__(name,price,model_year)
        self.battery= Battery("li",5)
    def car_capacity(self):
        self.battery.get_running_capacity()