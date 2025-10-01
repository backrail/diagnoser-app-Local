# 診断アプリ (Diagnoser App)

![screenshot](static/img/sample_quiz.jpg)

「診断をする」だけでなく「自分で診断を作れる」シンプルなWebアプリです。  
プログラミングが分からなくても、管理ページから診断を登録すればすぐに遊べます 🎉

---

## 🚀 使い方

### 1. Renderで遊ぶ（インストール不要）
以下のリンクをクリックするだけで、すぐに診断が遊べます。  
👉 [デモサイトはこちら](https://diagnoser-app-2.onrender.com)

※ 無料プランなので、最初に開くと数十秒かかることがあります。

---

### 2. 自分のPCで動かす（フル機能版）
アップロード機能なども使える、完全版です。  
以下の手順でインストールしてください。

#### 必要なもの
- Python 3.11 以上
- Git（なくても zip ダウンロードでOK）

#### 手順
```bash
# リポジトリをダウンロード
git clone https://github.com/ユーザー名/diagnoser-app-local.git
cd diagnoser-app-local

# 必要なライブラリをインストール
pip install -r requirements.txt

# データベースを初期化
python app_migrate.py

# デモ診断を投入（任意）
flask seed_demo

# アプリを起動
flask run
