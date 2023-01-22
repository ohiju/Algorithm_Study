import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

n = int(input())
list1 = list(map(int, input().split()))

def select(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
cnt = 0
for i in list1:
    if select(i):
        cnt += 1
print(cnt)