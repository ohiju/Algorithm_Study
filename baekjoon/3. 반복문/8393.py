import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

a = int(input())
sum = 0

for i in range(1,a+1):
    sum+=i
    
print(sum)