import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break