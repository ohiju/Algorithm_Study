import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

a,b = map(int, input().split())

if a>b:
    print(">")
elif a<b:
    print("<")
else: 
    print("==")