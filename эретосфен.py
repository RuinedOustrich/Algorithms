N = 100
p = [True] * N
p[0] = p[1] = False
for k in range (2,N):
    if p[k]:
        for m in range(2*k, N, k):
            p[m] = False
for k in range(N):
    print(k, '-', 'простое' if p[k] else 'составное')

