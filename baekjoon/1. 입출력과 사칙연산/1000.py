# 백준 문제들을 vscode에서 풀기 위해 만들어둔 tool

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

a,b = input().split()

print(int(a)+int(b))