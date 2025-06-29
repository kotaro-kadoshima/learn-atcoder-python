# atcoder_python

## 概要

- VSCode 上で AtCoder の Python3 および PyPy 環境を再現します。
- 自動テストや提出を行うためのツールとして、`atcoder-cli`と`online-judge-tools`を導入しています。
- 現状、コンテストのディレクトリ作成やサンプルコードのテストを実施までできますが、提出はできません。

## 前提条件

- VSCode の拡張機能「DevContainers」を使用します。

## 使用方法

1. リポジトリをクローン

   ```bash
   git clone https://github.com/gomatofu/atcoder_python.git
   ```

2. VSCode でクローンしたディレクトリを開く

   ```bash
   code atcoder_python
   ```

3. VSCode のコマンドパレットを開き、`Remote-Containers: Reopen in Container`を選択します。

## コンテストプロジェクトの作成方法

```
# contestディレクトリに移動
cd c
# コンテスト用のディレクトリを作成
acc new ${ContestName}
```

コンテスト名はコンテストサイト URL にあります。
`https://atcoder.jp/contests/◯◯◯◯◯`
こちらの`◯◯◯◯◯`にあたります。

## .env に REVEL_SESSION を記載

.env

```
ATCODER_REVEL_SESSION=${REVEL_SESSION}
```

REVEL_SESSION の取得方法は「2. **REVEL_SESSION クッキーを取得** 」を参考にしてください。

## ログイン方法

### 前提条件

- AtCoder のアカウントを作成していること

### ログイン手順

1. **AtCoder にログイン**  
   ブラウザで AtCoder にログインします。

2. **REVEL_SESSION クッキーを取得**  
   REVEL_SESSION クッキーは`httpOnly`属性が設定されているため、JavaScript から直接取得できません。以下の手順で手動で取得してください。

   - **Step 1: 開発者ツールを開く**  
     キーボードで`F12`キーを押すか、右クリックして「検証」または「Inspect」を選択します。

   - **Step 2: Application/Storage タブを開く**  
     開発者ツールの上部メニューから「Application」タブをクリックします。（Firefox の場合は「Storage」タブ）  
     左側のサイドバーから「Cookies」→「https://atcoder.jp」を選択します。

   - **Step 3: REVEL_SESSION の値をコピー**  
     クッキーの一覧から「REVEL_SESSION」という名前の行を探します。  
     「Value」列の値をダブルクリックして選択し、右クリックしてコピーするか、`Ctrl+C`（Mac なら`Cmd+C`）でコピーします。

3. **REVEL_SESSION クッキーの設定**\
   下記のコマンドを実行

   ```bash
   aclogin
   ```

   ```bash
   検知されたツール:
   - oj
   - acc
   AtCoder の REVEL_SESSION クッキーを貼り付けてください:
   ```

   とでるので、REVEL_SESSION を貼り付ける

   ```bash
   ✅ oj: クッキーを /home/vscode/.local/share/online-judge-tools/cookie.jar に保存しました
   ✅ acc: クッキーを /home/vscode/.config/atcoder-cli-nodejs/session.json に保存しました
   ✅ すべてのツール (2/2) にクッキーを保存しました
   ```

   と出力されれば完了

4. **コマンドを使用してログイン**  
   以下のコマンドを実行して、`atcoder-cli`および`online-judge-tools`でログイン作業を行います。

- `atcoder-cli`を使用してログイン:

  ```bash
  acc login
  ```

  実行後、AtCoder の`username`と`password`が求められるため、入力してください。（初回のみ必要）

- `online-judge-tools`を使用してログイン:
  ```bash
  oj login https://beta.atcoder.jp/
  ```
  実行後、AtCoder のログイン情報を入力してください。（初回のみ必要）

### 各種設定

#### acc の設定

```bash
# 問題インストール時に全問インストールされるように変更
acc config default-task-choice all
# デフォルトのテンプレートをpythonに変更
acc config default-template python
```

```bash
cd `acc config-dir`
mkdir python
cd python
touch template.json
touch main.py
code template.json
```

#### template.json の設定

```json
{
  "task": {
    "program": ["main.py"],
    "submit": "main.py"
  }
}
```

#### .bashrc の設定

```bash
code ~/.bashrc
```

追記内容

```bash
# PyPy3でのテスト実施
alias test='oj t -c "pypy3 main.py" -d ./tests/'
# Pythonでのテスト実施
alias test2='oj t -c "python3 main.py" -d ./tests/'
# PyPy3での解答提出
alias sb='acc s main.py -- --guess-python-interpreter pypy'
# Pythonでの解答提出
alias sb2='acc s main.py -- --language python'
# コンテストフォルダへ移動
alias c='cd contest'
# main.pyを開く
alias o='code main.py'
# 出力確認用
alias d='python main.py'
```

適用

```bash
source ~/.bashrc
```

