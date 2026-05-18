#父类
class Car:
    def __init__(self,brand,model,color, owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner

    def start(self):
        print(f"{self.brand} {self.model} is starting")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping")

    def __owner_info(self): #私有方法前面加两个下划线__
        print(f"{self.brand} {self.model} is owned by {self.__owner}")

    def charge(self):
        print(f"{self.brand} {self.model} is charging")

#子类
class FuelCar(Car):#获取父类非私有的属性和方法
    def __init__(self,brand,model,color,owner,fuel_type):
        super().__init__(brand,model,color,owner) #调用父类的构造函数
        self.fuel_type = fuel_type

    def charge(self):
        print(f"{self.brand} {self.model} 正在加油")


class ElectricCar(Car):
    def __init__(self,brand,model,color,owner,battery_size):
        super().__init__(brand,model,color,owner) #调用父类的构造函数
        self.battery_size = battery_size

    def charge(self):
        print(f"{self.brand} {self.model} 正在充电")

#多态：同一函数，根据不同的传入对象，执行不同的方法
#没有继承关系也可以使用多态
def handle_charge(car:Car):
    car.charge()

if __name__=="__main__":
    fc=FuelCar("Toyota","Corolla","Red","WQ","Gas")
    # fc.start()
    # fc.stop()

    ec=ElectricCar("Tesla","Model S","Black","WQ","100kWh")
    # ec.start()
    # ec.stop()

    handle_charge(fc)
    handle_charge(ec)