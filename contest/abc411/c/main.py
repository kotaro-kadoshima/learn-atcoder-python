N, Q = map(int, input().split())
A = list(map(int, input().split()))
math = [False] * N
count = 0

for i in range(Q):
    index = A[i] - 1
    math[index] = not math[index]

    left = math[index - 1] if index > 0 else False
    right = math[index + 1] if index < N - 1 else False

    if math[index]:
        if not left and not right:
            count += 1
        if left and right:
            count -= 1
    else:
        if not left and not right:
            count -= 1
        if left and right:
            count += 1

    print(count)
