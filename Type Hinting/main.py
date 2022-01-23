# ---------------------------------------- #
# 타입 Hinting
# def myfunction(myparameter): # 일반 함수
#     pass
# 파이썬은 변수 type이 자동적으로 변환이 가능해서 실행중에
# type을 알아내기가 어렵다. 그래서 Hinting을 사용한다.

def myfunction(myparameter: int) -> int:
    # return f"{myparameter}w + 10"
    return myparameter + 10

print(myfunction(10))
# pip install mypy
# 에러 코드 생성
# PS C:\Users\gksxo\Desktop\Folder\github\Advanced_Python_Tutorial\Type Hinting> mypy .\main.py
# main.py:11: error: Argument 1 to "myfunction" has incompatible type "str"; expected "int"
# Found 1 error in 1 file (checked 1 source file)

def otherfunction(otherparameter: str):
    print(otherparameter)

otherfunction(myfunction(20))


# def dosth(param: list[int]):
# list 힌트 사용법

# ---------------------------------------- #
