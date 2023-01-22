import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

n = int(input())
member_lst = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member_lst.append((age, name))

member_lst.sort(key = lambda x : x[0])	

for i in member_lst:
    print(i[0], i[1])