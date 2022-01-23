# ------------------------------------------------------ #
# 데코레이터 적용안한 상황
def mydecorator_no(function):

    def wrapper():
        function()
        print("I am decoration your function!")

    return wrapper()

def hello_world():
    print("hello! world")

# mydecorator_no(hello_world)
# ------------------------------------------------------ #


# ------------------------------------------------------ #
# 데코레이터 적용한 상황
def mydecorator_yes(function):

    def wrapper(*args, **kwargs): # 인잘르 받기 위해 *args, **kwargs 사용
        print("I am decoration your function!")
        return_value = function(*args, **kwargs)
        return return_value

    return wrapper

@mydecorator_yes
def hello(person):
    print(f"hello {person}!")
    return f"hello {person}!"

print(hello("Mike"))
# ------------------------------------------------------ #