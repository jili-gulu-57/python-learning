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


class HuaweiAiDriving:
    def __init__(self,version="v1.0"):
        self.version = version

    def start(self):
        print(f"Huawei Ai Driving {self.version} is starting")

#子类继承多个父类
class WenJieCar(Car,HuaweiAiDriving):
    def __init__(self,brand,model,color,owner,version):
        Car.__init__(self,brand,model,color,owner)
        HuaweiAiDriving.__init__(self,version)

if __name__=="__main__":
    #父类有多个同名方法时，按照顺序使用第一个
    car=WenJieCar("Honda","Civic","Black","WQ","v2.0")
    car.start()