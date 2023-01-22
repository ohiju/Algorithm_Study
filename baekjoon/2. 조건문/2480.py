import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

a,b,c = map(int, input().split())

if a!=b and b!=c and c!=a:
    print(max(a,b,c)*100)
    
elif a==b==c:
    print(10000+a*1000)
    
elif a==b!=c or b==c!=a or a==c!=b:
    if a==b:
        print(1000+a*100)
    elif b==c:
        print(1000+b*100)
    elif a==c:
        print(1000+a*100)