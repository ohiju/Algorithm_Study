import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 백준 코드 입력

import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque([])

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        queue.appendleft(command[1])
    elif command[0] == 'push_back':
        queue.append(command[1])
    elif command[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif command[0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
            queue.pop()
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] =='empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])