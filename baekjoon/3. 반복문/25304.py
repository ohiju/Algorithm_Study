import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

M = int(input())
N = int(input())
sum = 0

for i in range(N):
    a,b = map(int, input().split())
    sum += a*b
    
if sum == M:
    print("Yes")
elif sum != M:
    print("No") 