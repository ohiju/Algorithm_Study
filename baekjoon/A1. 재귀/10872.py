import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

n = int(input())
def factorial(n):
    out = 1
    if n>0:
        out = n*factorial(n-1)
    return out
print(factorial(n))