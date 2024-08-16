from collections import deque

def Deque(d):

    for i in range(N):
        D = list(input().split())
        if D[0] == 'append':
            d.append(D[1])
        elif D[0] == 'appendleft':
            d.appendleft(D[1])
        elif D[0] == 'pop':
            d.pop()
        else:
            d.popleft()
    print(' '.join(d))


if __name__ == '__main__':
    N = int(input())
    d = deque()
    Deque(d)