n = int(input())
cards = list(map(int, input().split()))

flg = True
alice = 0
bob = 0
for i in range(n):
    index = 0
    max = cards[index]
    for j in range(len(cards)):
        if max < cards[j]:
            index = j
            max = cards[j]
    cards.pop(index)

    if flg:
        alice += max
    else:
        bob += max
    flg = not flg

print(alice - bob)
