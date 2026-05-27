# 抽象类是一种不能直接实例化的类，它必须被继承，并且继承它的子类必须实现抽象类中的抽象方法
from abc import ABCMeta, abstractmethod, ABC


# 继承ABC类才是抽象类
# class Animal(ABC):
class Animal(metaclass=ABCMeta):
    # 抽象方法使用abstractmethod装饰器装饰
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Dog(Animal):
    def eat(self):
        print("狗吃骨头")

    def sleep(self):
        print("狗睡觉")


dog = Dog()
dog.eat()


class Cat(Animal):
    def sleep(self):
        print("猫睡觉")
        pass

    def eat(self):
        print("猫吃鱼")


cat = Cat()
cat.sleep()

# cat1=Animail()
# cat1.eat()
