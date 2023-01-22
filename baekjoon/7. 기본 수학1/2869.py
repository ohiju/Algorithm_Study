import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

import math
a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(math.ceil(k))