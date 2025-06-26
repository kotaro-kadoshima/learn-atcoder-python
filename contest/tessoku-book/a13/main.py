N, K = map(int, input().split())
A = list(map(int, input().split()))
R = [0] * N

for i in range(0, N - 1):
    # i=0であればR[i]=0から、そうでなければR[i]=R[i-1]からスタートする
    if i == 0:
        R[i] = i
    else:
        R[i] = R[i - 1]
    # 差分がA[R[i]]-A[i]がKを超えないギリギリまで、R[i]を1増やす
    while R[i] < N - 1 and A[R[i] + 1] - A[i] <= K:
        R[i] += 1

result = 0
# (R[N-1]-(N-1))
for i in range(0, N - 1):
    result += R[i] - i

print(result)
