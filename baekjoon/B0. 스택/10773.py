import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

import sys
K = int(sys.stdin.readline())
stack = []

for i in range(K):
    new_in = int(sys.stdin.readline())
    if new_in == 0:
        stack.pop()
    else:
        stack.append(new_in)

print(sum(stack))