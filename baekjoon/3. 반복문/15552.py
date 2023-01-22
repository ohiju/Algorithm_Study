import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

import sys
T = int(input())

for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)