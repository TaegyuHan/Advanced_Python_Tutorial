# ------------------------------------------------------ #
class Person:

    def __init__(self, name, age):
        """생성 매직 메소드"""
        self.name = name
        self.age = age

    def __del__(self):
        """삭제 매직 메소드"""
        print("Object is being deconstructed!")

# ------------------------------------------------------ #
p = Person("Mike", 25)
del p

# ------------------------------------------------------ #
class Vector:

    def __init__(self, x, y):
        """생성 매직 메소드"""
        self.x = x
        self.y = y

    def __add__(self, other):
        """인스턴스 끼리 더해주는 매직 메소드"""
        return Vector(self.x + other.x, self.y + other.y)

    # Python 버전
    def __repr__(self):
        """print 함수 출력 적용"""
        return f"X: {self.x}, Y: {self.y}"

    # 자바 버전!!
    def to_string(self):
        return f"X: {self.x}, Y: {self.y}"

    def __len__(self):
        """길이 출력"""
        return 10

    def __call__(self, *args, **kwargs):
        "인스턴스를 불렀을 떄 작동"
        print("Hello! I was called!")

v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2
print(v3)
print(len(v3))
v3()
# ------------------------------------------------------ #