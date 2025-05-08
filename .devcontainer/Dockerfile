# .devcontainer/Dockerfile

# 1) ベースを新しく
FROM python:3.11-slim

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

# 2) 必要なビルドツールを追加（SciPy / numba 等のソースビルド対策も兼ねる）
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential gfortran libopenblas-dev liblapack-dev \
        pypy3 nodejs npm sudo && \
    rm -rf /var/lib/apt/lists/*

# 3) sudo やユーザー作成
RUN groupadd --gid ${USER_GID} ${USERNAME} && \
    useradd -m -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} ${USERNAME} && \
    echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME} && \
    chmod 0440 /etc/sudoers.d/${USERNAME}

# 4) Python ライブラリ
COPY requirements.txt /tmp/
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

# 5) AtCoder 用ツール
RUN pip install --no-cache-dir online-judge-tools && \
    npm install -g atcoder-cli