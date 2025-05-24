n = int(input())
a = list(map(int, input().split()))

for a1 in a:
    for a2 in a:
        if a1 == a2:
            continue
        for a3 in a:
            if a1 == a3 or a2 == a3:
                continue
            if a1 + a2 + a3 == 1000:
                print("Yes")
                exit()
print("No")
