N, K = map(int, input().split())
A = list(map(int, input().split()))
R = [0] * N


for i in range(N):
    r = 0
    if 0 < i:
        r = i - 1
    if A[r] - A[i] <= K:
        print(A[r])
