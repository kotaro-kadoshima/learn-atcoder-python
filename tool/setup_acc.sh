#!/bin/bash
# accツールのログイン
# python python aclogin_custom.py

# accの設定
acc config default-task-choice all
acc config default-template python

# テンプレートディレクトリ・ファイル作成
cd "$(acc config-dir)"
mkdir -p python
cd python
touch template.json
touch main.py

# template.jsonの設定
cat > template.json <<EOF
{
  "task": {
    "program": ["main.py"],
    "submit": "main.py"
  }
}
EOF

# .bashrcにエイリアスを追記（重複防止）
BASHRC="$HOME/.bashrc"
ALIASES=$(cat <<'EOL'
# PyPy3でのテスト実施
alias test='oj t -c "pypy3 main.py" -d ./tests/'
# Pythonでのテスト実施
alias test2='oj t -c "python3 main.py" -d ./tests/'
# PyPy3での解答提出
alias sb='acc s main.py -- --guess-python-interpreter pypy'
# Pythonでの解答提出
alias sb2='acc s main.py'
# コンテストフォルダへ移動
alias c='cd /atcoder_python/contest'
# main.pyを開く
alias o='code main.py'
# 出力確認用
alias d='python main.py'
EOL
)

if ! grep -q "alias test=" "$BASHRC"; then
  echo "$ALIASES" >> "$BASHRC"
fi

# # .bashrcを再読み込み
source "$BASHRC"

echo "acc設定・テンプレート・エイリアスのセットアップが完了しました。"
