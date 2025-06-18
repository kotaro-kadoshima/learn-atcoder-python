def match(target, answer):
    if target == answer:
        return True
    return False


def del_search(s):
    del_list = set()
    H = len(s)
    W = len(s[0])
    for i in range(H):
        for j in range(W):
            num = s[i][j]
            if num == ".":
                continue  # 空マスはスキップ

            # 上下右左で判定していく
            if i != 0:
                if not match(s[i - 1][j], num):
                    continue

            if i != H - 1:
                if not match(s[i + 1][j], num):
                    continue

            if j != W - 1:
                if not match(s[i][j + 1], num):
                    continue

            if j != 0:
                if not match(s[i][j - 1], num):
                    continue

            # del_listに詰める

            del_list.add((i, j))
            if i != 0:
                del_list.add((i - 1, j))
            if i != H - 1:
                del_list.add((i + 1, j))
            if j != W - 1:
                del_list.add((i, j + 1))
            if j != 0:
                del_list.add((i, j - 1))
    return del_list


def del_point(s, del_list):
    # 文字列リストをリストのリストに変換
    s_list = [list(row) for row in s]
    for i, j in del_list:
        s_list[i][j] = "."
    # 再び文字列リストに戻す
    return ["".join(row) for row in s_list]


def move(s):
    H = len(s)
    W = len(s[0])
    # 下から2番目から探索して、ブロックを移動させる
    for i in range(H - 2, -1, -1):
        for j in range(W):
            num = s[i][j]
            if num == ".":
                continue

            search_index = i
            while True:
                # 最下段であれば抜ける
                if search_index == H - 1:
                    break

                # 移動先が空であれば移動
                if s[search_index + 1][j] == ".":
                    # 文字列をリストに変換して入れ替え
                    s_list = list(s[search_index])
                    s_list[j] = "."
                    s[search_index] = "".join(s_list)
                    s_list = list(s[search_index + 1])
                    s_list[j] = num
                    s[search_index + 1] = "".join(s_list)
                    search_index += 1
                else:
                    # 空じゃなければ抜ける
                    break
    return s


H = int(input())
S = [""] * H
for i in range(H):
    S[i] = input()
while True:
    del_list = del_search(S)
    if len(del_list) == 0:
        break
    S = del_point(S, del_list)
    S = move(S)

for i in range(H):
    print(S[i])
