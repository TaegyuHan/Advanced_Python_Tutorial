# ------------------------------------------------------ #
# Seq 1 to 9,000,000
import sys

def mygenerator(n):
    for x in range(n):
        yield x ** 3

# values = mygenerator(9_000_000)
# print(f"byte: {sys.getsizeof(values)}")
# 사용메모리 확인

# for x in values:
#     print(x)
# ------------------------------------------------------ #


# ------------------------------------------------------ #
def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()
# for x in values:
#     print(x)

# ------------------------------------------------------ #
