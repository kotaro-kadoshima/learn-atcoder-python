# Python文法・注意点まとめ

## 1. リストの要素追加
- `list.add()` は存在しない。リストには `append()`、セットには `add()` を使う。
  - 例:
    ```python
    mylist = []
    mylist.append((i, j))
    myset = set()
    myset.add((i, j))
    ```

## 2. 文字列の要素代入
- 文字列（str型）はイミュータブル。`s[i][j] = "."` のような直接代入は不可。
- 文字列をリストに変換して編集し、再度 `"".join()` で文字列に戻す必要がある。
  - 例:
    ```python
    s = "12345"
    s_list = list(s)
    s_list[2] = "."
    s = "".join(s_list)  # '12.45'
    ```

## 3. リストのインデックス範囲外アクセス
- 存在しないインデックスに直接代入すると `IndexError`。
- 必要な長さで初期化してから使う。
  - 例:
    ```python
    a = [0] * 10
    a[5] = 1  # OK
    # a[10] = 1  # IndexError
    ```

## 4. len()の使い方
- `len()` はリストや文字列などシーケンス型に使う。int型には使えない。
  - 例:
    ```python
    len([1,2,3])  # 3
    len("abc")   # 3
    # len(10)    # NG: TypeError
    ```

## 5. グローバル変数とローカル変数
- 関数内でグローバル変数を参照する場合、引数で渡す方が安全。
- 例:
    ```python
    def func(s):
        H = len(s)
        # ...
    ```

## 6. 2次元リストのサイズ
- `[[0]*W for _ in range(H)]` でH×Wの2次元リストを作る。
  - 例:
    ```python
    H, W = 3, 4
    grid = [[0]*W for _ in range(H)]
    # grid[1][2] = 5
    ```

## 7. for文の範囲
- `range(開始, 終了, 増分)` でループ範囲を指定。
- 例:
    ```python
    for i in range(H-2, -1, -1):  # 下から上へ
        ...
    ```

## 8. continue/breakの使い方
- `continue`は次のループへ、`break`はループを抜ける。
  - 例:
    ```python
    for i in range(5):
        if i % 2 == 0:
            continue
        if i == 3:
            break
        print(i)
    # 出力: 1
    ```

## 9. 変数名の衝突
- `list`や`str`など組み込み型名を変数名にしない。
  - 例:
    ```python
    # NG: list = [1,2,3]
    nums = [1,2,3]  # OK
    ```

## 10. 2次元リストの可変列数対応
- 列数は `W = len(s[0])` で取得し、`range(W)` でループ。
  - 例:
    ```python
    for j in range(len(s[0])):
        ...
    ```

---

このまとめは、今回のプログラム修正で気づいたPythonの文法や注意点です。
