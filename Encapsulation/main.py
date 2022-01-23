# ---------------------------------------- #
# 캡슐화 #
class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property # 캡슐화 방법 getter
    def Name(self):
        return self.__name

    @Name.setter # 캡슐화 방법 setter
    def Name(self, value):
        if value == "Bob":
            self.__name = "Default Name"
        else:
            self.__name = value

    @staticmethod
    def mymethod():
        print("Hello World!")

Person.mymethod()

p1 = Person("Mike", 20, "m")
print(p1.Name)

Person.mymethod()

p1.Name = "Bob"
print(p1.Name)