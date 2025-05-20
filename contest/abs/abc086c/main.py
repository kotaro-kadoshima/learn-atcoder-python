N = int(input())
t = [0]
x = [0]
y = [0]

for _ in range(N):
    ti, xi, yi = map(int, input().split())
    t.append(ti)
    x.append(xi)
    y.append(yi)

can = True
for i in range(N):
    # 今の地点から次の地点に行くまでの 時間の猶予（使える秒数）
    dt = t[i + 1] - t[i]
    # マンハッタン距離（1マスずつ動くときの最短移動距離）
    dist = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])

    # dt（使える秒数）が dist（最低必要移動距離）より小さいとダメ
    # (dt - dist) が偶数であること
    if dt < dist or (dt - dist) % 2 != 0:
        can = False
        break

print("Yes" if can else "No")
