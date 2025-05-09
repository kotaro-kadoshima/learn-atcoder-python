# atcoder_python

## 概要
- VSCode上でAtCoderのPython3およびPyPy環境を再現します。
- 自動テストや提出を行うためのツールとして、`atcoder-cli`と`online-judge-tools`を導入しています。

## 前提条件

- VSCodeの拡張機能「DevContainers」を使用します。

## 使用方法

1. リポジトリをクローン

   ```bash
   git clone https://github.com/gomatofu/atcoder_python.git
   ```

2. VSCodeでクローンしたディレクトリを開く

   ```bash
   code atcoder_python
   ```

3. VSCodeのコマンドパレットを開き、```Remote-Containers: Reopen in Container```を選択します。

## ログイン方法

### 前提条件
- AtCoderのアカウントを作成していること

### ログイン手順

1. **AtCoderにログイン**  
   ブラウザでAtCoderにログインします。

2. **REVEL_SESSIONクッキーを取得**  
   REVEL_SESSIONクッキーは`httpOnly`属性が設定されているため、JavaScriptから直接取得できません。以下の手順で手動で取得してください。

   - **Step 1: 開発者ツールを開く**  
     キーボードで`F12`キーを押すか、右クリックして「検証」または「Inspect」を選択します。

   - **Step 2: Application/Storageタブを開く**  
     開発者ツールの上部メニューから「Application」タブをクリックします。（Firefoxの場合は「Storage」タブ）  
     左側のサイドバーから「Cookies」→「https://atcoder.jp」を選択します。

   - **Step 3: REVEL_SESSIONの値をコピー**  
     クッキーの一覧から「REVEL_SESSION」という名前の行を探します。  
     「Value」列の値をダブルクリックして選択し、右クリックしてコピーするか、`Ctrl+C`（Macなら`Cmd+C`）でコピーします。

3. **`acc`の`session.json`ファイルを編集**  
   以下のコマンドで`session.json`ファイルを開き、REVEL_SESSIONの値を設定します。

   ```bash
   code /home/vscode/.config/atcoder-cli-nodejs/session.json
   ```

4. **`oj`の`cookie.jar`ファイルを編集**  
   以下のコマンドで`cookie.jar`ファイルを開き、REVEL_SESSIONの値を設定します。

   ```bash
   code /home/vscode/.local/share/online-judge-tools/
   ```
5. **コマンドを使用してログイン**  
以下のコマンドを実行して、`atcoder-cli`および`online-judge-tools`でログイン作業を行います。

- `atcoder-cli`を使用してログイン:
    ```bash
    acc login
    ```
    実行後、AtCoderの`username`と`password`が求められるため、入力してください。（初回のみ必要）

- `online-judge-tools`を使用してログイン:
    ```bash
    oj login https://beta.atcoder.jp/
    ```
    実行後、AtCoderのログイン情報を入力してください。（初回のみ必要）
