import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

N = int(input())

arr = []

for _ in range(N) : 
    arr.append(int(input()))

for i in range(1, len(arr)):
    for j in range(i, 0, -1): 
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
            
for n in arr : 
    print(n)