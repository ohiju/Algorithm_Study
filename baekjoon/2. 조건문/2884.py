import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

a,b = map(int, input().split())

if b>=45:
    b-=45
    print(a,b)
        
elif a>0 and b<45:
    a-=1
    b=(60-(45-b))
    print(a,b)
    
elif a==0 and b<45:
    a=23
    b=(60-(45-b))
    print(a,b)   