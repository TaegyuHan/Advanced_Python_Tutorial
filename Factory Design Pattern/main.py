# ------------------------------------------------------ #
from abc import ABCMeta, abstractstaticmethod # 추상 메소드 사용하기

# 인터페이스 클래스는 I대문자를 붙여준다.
# meta=ABCMeta 인스턴스를 생성 못하게 한다.
class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface Method """

class Student(IPerson):

    def __init__(self):
        self.name = "Basic Student Name"

    def person_method(self):
        print("I am a student")

class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teachar Name"

    def person_method(self):
        print("I am a teacher")

class PersonFactory:

    @staticmethod
    def build_person(person_tyep: str):
        if person_tyep == "Student":
            return Student()
        elif person_tyep == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1

if __name__ == '__main__':
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory().build_person(choice)
    person.person_method()

# s1 = Student()
# s1.person_method()
#
# t1 = Student()
# t1.person_method()

# p1 = IPerson()
# p1.person_method()
# 추상 메소드를 인스턴스로 생성하면 에러가 발생한다.
# Traceback (most recent call last):
#   File "C:\Users\gksxo\Desktop\Folder\github\Advanced_Python_Tutorial\Factory Design Pattern\main.py", line 12, in <module>
#     p1 = IPerson()
# TypeError: Can't instantiate abstract class IPerson with abstract method person_method
# ------------------------------------------------------ #