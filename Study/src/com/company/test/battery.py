class Battery():
    def __init__(self, battery_type,no_of_battery=3):
        self.no_of_battery= no_of_battery
        self.battery_type= battery_type
    def get_running_capacity(self):
        if self.no_of_battery ==5:
            print("car can run up to 500 on full charge")
        else:
            print("car can run up to 100 on full charge") 