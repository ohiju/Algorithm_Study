import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

n = int(input())

beeHouse = 1
c = 1

while n>beeHouse:
    beeHouse += 6*c
    c += 1
    
print(c)
    