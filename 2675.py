T = int(input())
result =''
for i in range(T):
    N = list(map(str, input().split()))
    M = int(N[0])
    A = list(map(str, N[1]))

    for j in range(len(A)):
        for k in range(M):
            print(A[j], end='')
    print('')
