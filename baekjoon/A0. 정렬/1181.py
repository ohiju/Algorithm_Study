import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

N = int(input())
a = []
for _ in range(N):
    a.append(input())

set_a = set(a)
a = list(set_a)	
a.sort()
a.sort(key = len)

for i in a:
    print(i)