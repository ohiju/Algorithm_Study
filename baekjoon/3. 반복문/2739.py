import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

a = int(input())

for i in range(1,10):
    print(a,"*",i,"=",a*i)