s = input()

word_list = ["dream", "dreamer", "erase", "eraser"]
word_list = [word[::-1] for word in word_list]

s = s[::-1]

flg = True
start_flg = False
while flg:
    for name in word_list:
        if s.startswith(name):
            start_flg = True
            # 「:」はスライス記法　文字数分切り捨てる
            s = s[len(name) :]
            if len(s) == 0:
                print("YES")
                exit()
    if start_flg:
        start_flg = False
        continue
    flg = False

print("NO")
