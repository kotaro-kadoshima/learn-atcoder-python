N = int(input())

# 後ろから始める
for i in range(9, -1, -1):
    print(N // (2**i) % 2, end="")

print("")
