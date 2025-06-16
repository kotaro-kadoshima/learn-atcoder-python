N, X = map(int, input().split())
A = list(map(int, input().split()))


def search(x, A):
    L = 0
    R = len(A) - 1
    while L <= R:
        M = (L + R) // 2
        if x < A[M]:
            R = M - 1
        elif x > A[M]:
            L = M + 1
        elif x == A[M]:
            return M
    return -1


answer = search(X, A)
print(answer + 1)
