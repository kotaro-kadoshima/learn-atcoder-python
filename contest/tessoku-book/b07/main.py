T = int(input())
N = int(input())

sum = [0] * (T + 1)

for i in range(N):
    L, R = map(int, input().split())
    sum[L] += 1
    sum[R] -= 1

tmp = 0
for t in range(T):
    tmp += sum[t]
    print(tmp)
