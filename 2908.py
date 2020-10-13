N = list(map(int, input().split()))
data = [0]*2
for i in range(len(N)):
    M = list(map(str, str(N[i])))
    M[0], M[2] = M[2], M[0]
    data[i] = int(M[0]+M[1]+M[2])

if(data[0] > data[1]):
    print(data[0])
else:
    print(data[1])
