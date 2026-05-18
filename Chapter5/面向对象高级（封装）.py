class Car:
    def __init__(self,brand,model,color,owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner= owner #私有属性前面加双下划线__

    def start(self):
        print(f"{self.brand} {self.model} is starting")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping")

    def __owner_info(self): #私有方法前面加两个下划线__
        print(f"{self.brand} {self.model} is owned by {self.__owner}")


if __name__=="__main__":
    car = Car("Toyota","Corolla","Red","WQ")
    print(f"car brand:{car.brand}")
    print(f"car model:{car.model}")
    print(f"car color:{car.color}")
    # print(f"car owner:{car.__owner}")
    print(f"car owner:{car._Car__owner}")

    car.start()
    car.stop()

    #并无真正私有机制，仅是一种语法约定
    # car.__owner_info()
    car._Car__owner_info()
