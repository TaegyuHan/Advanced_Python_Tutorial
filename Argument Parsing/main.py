# ------------------------------------------------------ #
# python3 myscript.py result.txt
# python3 myscript.py -o test.txt -l DEBUG -c

# 인자 파싱
def myfunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs["KEYONE"])
    print(kwargs["KEYTWO"])

myfunction('hey', True, 19, "wow", KEYONE="TEST", KEYTWO="7")

# ------------------------------------------------------ #

# ------------------------------------------------------ #
import sys
print(sys.argv) # 모든인자 확인해보기
print(sys.argv[0]) # file_name
print(sys.argv[1]) # 다음 명령어

# ------------------------------------------------------ #

# ------------------------------------------------------ #
# python 인터프리터 실행 파일 인자 받기 ( 직접 제작 )
import sys

# Usage: main.py FILENAME -p 8080 -h localhost
filename = sys.argv[1]
message = sys.argv[2]

with open(filename, "w+") as f:
    f.write(message)
# ------------------------------------------------------ #

# ------------------------------------------------------ #
# python 인터프리터 실행 파일 인자 받기 ( 라이브러리 이용 )
import sys
import getopt

opts, args = getopt.getopt(sys.argv[1:], "f:m:t", ["filename", "message"])
print(opts)
print(args)

# > Terminal
# > python .\main.py test.txt 1234
# []
# ['test.txt', '1234']

# > Terminal
# > python .\main.py -f test.txt -m Hello\ World
# [('-f', 'test.txt'), ('-m', 'Hello\\')]
# ['World']

for opt, arg in opts:
    if opt == "-f":
        filename = arg
    if opt == "-m":
        message = arg

with open(filename, "w+") as f:
    f.write(message)
# ------------------------------------------------------ #