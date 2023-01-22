import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

a,b = input().split()

print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)//int(b))
print(int(a)%int(b))