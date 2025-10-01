from __future__ import annotations

import os
from flask import Flask
from dotenv import load_dotenv

from app_migrate import run_auto_migrations
from blueprints.admin.routes import bp as admin_bp
from blueprints.public.routes import bp as public_bp
from config import Config
from extensions import db
from models import User
from datetime import datetime

def create_app() -> Flask:
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(Config)

    # ---- ファイルアップロード設定 ----
    # /static/uploads に保存（存在しなければ作成）
    app.config["UPLOAD_FOLDER"] = os.path.join("static", "uploads")
    app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg", "gif", "webp"}
    app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024  # 2MB
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # ---- DB 初期化＆簡易マイグレーション ----
    db.init_app(app)
    with app.app_context():
        db.create_all()
        run_auto_migrations()

        admin = User.query.filter_by(username="admin").first()
        if admin and os.getenv("ADMIN_PASSWORD"):
            from werkzeug.security import generate_password_hash

            admin.password_hash = generate_password_hash(
                os.getenv("ADMIN_PASSWORD")
            )
            db.session.commit()

    @app.context_processor
    def inject_current_year():
        return {"current_year": datetime.now().year}

    # ---- Blueprint 登録 ----
    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp)

    # ---- 便利CLI ----
    @app.cli.command("seed")
    def seed_command() -> None:
        """ライトS/M傾向診断のデモデータ投入"""
        from seed import seed  # 遅延 import で循環回避

        seed()

    return app


app = create_app()
