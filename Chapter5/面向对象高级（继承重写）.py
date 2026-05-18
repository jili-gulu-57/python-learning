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

#子类
class FuelCar(Car):#获取父类非私有的属性和方法
    def __init__(self,brand,model,color,owner,fuel_type):
        super().__init__(brand,model,color,owner) #调用父类的构造函数
        self.fuel_type = fuel_type

    def refuel(self):
        print(f"{self.brand} {self.model} is refueling")

    def start(self):#重写父类的方法(同名即重写)
        print(f"{self.brand} {self.model} 正在启动")


if __name__=="__main__":
    fc=FuelCar("Toyota","Corolla","Red","WQ","Gas")
    fc.start()
    fc.stop()
