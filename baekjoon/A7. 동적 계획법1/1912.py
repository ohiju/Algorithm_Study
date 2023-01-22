import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

n = int(input())
a = list(map(int, input().split()))
sum = [a[0]]
for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
print(max(sum))