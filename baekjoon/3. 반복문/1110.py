import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

import sys
N = sys.stdin.readline().rstrip()
cnt = 0

if int(N)<10:
    N = str(0)+N

answer = N

while True:
    N = N[-1] +(str(int(N[0])+int(N[-1])))[-1]
    cnt+=1
        
    if answer == N : 
        break
print(cnt)