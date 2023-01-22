import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력
numbers = [int(input()) for _ in range(10)]

for i in range(len(numbers)):
    numbers[i] = numbers[i]%42
    
    
print(len(set(numbers)))

