import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

for i in range(9999):
    a,b = map(int, input().split())
    if a==b==0:
        break
    print(a+b)