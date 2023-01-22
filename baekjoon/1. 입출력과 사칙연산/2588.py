import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

a= int(input())
b= int(input())

x1 = a*int(str(b)[2])
x2 = a*int(str(b)[1])
x3 = a*int(str(b)[0])
x4 = a*b

print(x1)
print(x2)
print(x3)
print(x4)