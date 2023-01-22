import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

N = int(input())

score = list(map(int, input().split()))
a=max(score)

for i in range(len(score)):
    score[i] = score[i]/a*100
    
print(sum(score)/N)