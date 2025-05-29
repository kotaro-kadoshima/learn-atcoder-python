D = int(input())
N = int(input())

sum = [0] * D
for i in range(N):
    L, R = map(int, input().split())
    sum[L - 1] += 1
    if R != D:
        sum[R] -= 1

result = 0
for i in range(D):
    result += sum[i]
    print(result)
