import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

a = [1, 1, 2, 2, 2, 8]
b = list(map(int, input().split()))

for i in range(6):
    print(a[i]-b[i], end=' ')