import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

n = int(input())
sum = 0
a = input()

for i in range(n):
    sum += int(a[i])
    
print(sum)