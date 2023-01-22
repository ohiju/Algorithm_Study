import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

a = int(input())

for i in range(a):
    print((" ")*(a-i-1)+("*")*(i+1))