# ------------------------------------------------------ #
from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    """ Person 추상 클래스 """
    @abstractstaticmethod
    def person_method():
        """ person 추상 메소드 """

class Person(IPerson):

    def person_method(self):
        print("I am a person!")

class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am the proxy functionality!")
        self.person.person_method()

p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()

# ------------------------------------------------------ #