import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

T = int(input())

for i in range(T):
    A,B = map(int, input().split())
    C=A+B
    print("Case #",i+1,": ",A," + ",B," = ",C, sep='')