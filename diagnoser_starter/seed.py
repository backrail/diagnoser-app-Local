from __future__ import annotations

from extensions import db
from models import Choice, Question, Quiz, Result, User


# ============================================================
# カエルのことどれだけ知ってる？最上級テスト（15問）
#   - 正答のみ加点（各1点）
#   - 合否判定：12点以上で合格
#   - 表示順は管理順（ordered）を前提
# ============================================================
def seed(db_uri_print: bool = False) -> None:
    """カエル知識・最上級テスト（簡単そうで難しい上級編）"""
    if db_uri_print:
        try:
            print(f"[seed] DB = {db.engine.url}")
        except Exception:
            pass

    # 管理ユーザー作成（なければ）
    if not User.query.filter_by(username="admin").first():
        from werkzeug.security import generate_password_hash

        admin = User(username="admin", password_hash=generate_password_hash("admin123"))
        db.session.add(admin)
        db.session.flush()

    title = "カエルのことどれだけ知ってる？最上級テスト（15問）"
    old = Quiz.query.filter_by(title=title).first()
    if old:
        db.session.delete(old)
        db.session.flush()

    quiz = Quiz(
        title=title,
        description=(
            "一見やさしそうで実は難しい、カエル知識の上級テストです。\n"
            "各問の正解のみが得点となります（誤答は加点なし）。\n"
            "12点以上で合格。あなたは“カエル博士”になれるか？"
        ),
    )
    if hasattr(quiz, "display_mode"):
        quiz.display_mode = "ordered"
    db.session.add(quiz)
    db.session.flush()

    order = 0

    # --- Q1 ---
    q = Question(
        quiz=quiz,
        text="カエルは分類学上どの『目（Order）』に属する？",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(question=q, text="無尾目（Anura）", sum_points=1),
            Choice(question=q, text="有尾目（Urodela）", sum_points=0),
            Choice(question=q, text="爬虫目（Squamata）", sum_points=0),
        ]
    )

    # --- Q2 ---
    q = Question(
        quiz=quiz,
        text="多くのカエルで見られる鼓膜（外鼓膜）はどこにある？",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(question=q, text="眼のすぐ後ろの皮膚表面", sum_points=1),
            Choice(question=q, text="上顎の内側（口腔内）", sum_points=0),
            Choice(question=q, text="背中の中央付近", sum_points=0),
        ]
    )

    # --- Q3 ---
    q = Question(
        quiz=quiz,
        text="一部のカエルは、内容物を取り除くために胃を『反転（外へ裏返す）』できる。",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(question=q, text="正しい", sum_points=1),
            Choice(question=q, text="誤り", sum_points=0),
        ]
    )

    # --- Q4 ---
    q = Question(
        quiz=quiz,
        text="モリアオガエルの代表的な産卵様式として正しいのはどれ？",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(
                question=q,
                text="水面上の枝などに泡状の巣（泡巣）を作り、そこから孵化したオタマを水中へ落とす",
                sum_points=1,
            ),
            Choice(question=q, text="川底に硬い殻の卵を一粒ずつ産む", sum_points=0),
            Choice(question=q, text="砂丘上に産卵し風で散らす", sum_points=0),
        ]
    )

    # --- Q5 ---
    q = Question(
        quiz=quiz,
        text="オタマジャクシの一般的な消化器の特徴として最も適切なのは？",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(
                question=q,
                text="長い腸をもち、植物質中心の食性に適応している種が多い",
                sum_points=1,
            ),
            Choice(question=q, text="完全に無胃で、消化は口腔でのみ行う", sum_points=0),
            Choice(question=q, text="短い腸で高タンパク捕食に特化が一般的", sum_points=0),
        ]
    )

    # --- Q6 ---
    q = Question(
        quiz=quiz,
        text="カエルの歯について正しい記述はどれ？",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(
                question=q,
                text="上顎に小さな歯（鋤骨歯など）を持つが、下顎は無歯が基本",
                sum_points=1,
            ),
            Choice(question=q, text="上下とも臼歯が発達している", sum_points=0),
            Choice(question=q, text="乳歯から永久歯に生え替わる", sum_points=0),
        ]
    )

    # --- Q7 ---
    q = Question(
        quiz=quiz,
        text="ニホンアマガエルの鳴嚢（鳴き袋）に関する正しい説明はどれ？",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(
                question=q,
                text="喉の中央に1つ（正中位）膨らむ単一鳴嚢で共鳴する",
                sum_points=1,
            ),
            Choice(question=q, text="左右一対の外側鳴嚢が基本", sum_points=0),
            Choice(question=q, text="鳴嚢は雌のみに見られる", sum_points=0),
        ]
    )

    # --- Q8 ---
    q = Question(
        quiz=quiz,
        text="多くのカエルで一般的な交接様式（抱接）はどれ？",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(question=q, text="腋下抱接（オスが雌の前肢付け根を抱える）", sum_points=1),
            Choice(question=q, text="腰抱接（雌の腰部を抱える）が圧倒的に主流", sum_points=0),
            Choice(question=q, text="尾抱接（尾を絡める）が一般的", sum_points=0),
        ]
    )

    # --- Q9 ---
    q = Question(
        quiz=quiz,
        text="成体カエルのガス交換について最も適切な説明はどれ？",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(
                question=q,
                text="肺呼吸に加え、皮膚呼吸の寄与が大きく、低温時などは皮膚呼吸の比率が増える",
                sum_points=1,
            ),
            Choice(question=q, text="成体では皮膚呼吸は完全に退化する", sum_points=0),
            Choice(question=q, text="エラ呼吸が主で肺は痕跡器官", sum_points=0),
        ]
    )

    # --- Q10 ---
    q = Question(
        quiz=quiz,
        text="ニホンアマガエルの越冬（冬眠）場所として最も一般的なのは？",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(question=q, text="落ち葉の下や土中など陸上の隙間", sum_points=1),
            Choice(question=q, text="湖底の深水域に長期潜水", sum_points=0),
            Choice(question=q, text="樹洞内の水たまりで完全水中生活", sum_points=0),
        ]
    )

    # --- Q11 ---
    q = Question(
        quiz=quiz,
        text="オタマジャクシの変態を強力に促進するホルモンはどれ？",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(question=q, text="甲状腺ホルモン（チロキシン/T4 など）", sum_points=1),
            Choice(question=q, text="インスリン", sum_points=0),
            Choice(question=q, text="メラトニン", sum_points=0),
        ]
    )

    # --- Q12 ---
    q = Question(
        quiz=quiz,
        text="オスに見られる『婚姻瘤（拇指丘）』の役割として適切なのは？",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(question=q, text="抱接時に雌をしっかり保持するため", sum_points=1),
            Choice(question=q, text="敵の毒を分泌する器官", sum_points=0),
            Choice(question=q, text="体温調節の放熱板", sum_points=0),
        ]
    )

    # --- Q13 ---
    q = Question(
        quiz=quiz,
        text="日本各地で定着して問題となった外来カエルとして最も適切なのは？",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(question=q, text="ウシガエル（アメリカ原産）", sum_points=1),
            Choice(question=q, text="ガラスガエル（中南米原産）", sum_points=0),
            Choice(question=q, text="アフリカツメガエル（研究用のみで野外定着なし）", sum_points=0),
        ]
    )

    # --- Q14 ---
    q = Question(
        quiz=quiz,
        text="多くのカエルの発声メカニズムとして正しいのはどれ？",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(
                question=q,
                text="肺の空気を喉頭の声帯に往復させ、鳴嚢で共鳴させるため口を閉じたままでも鳴ける",
                sum_points=1,
            ),
            Choice(question=q, text="舌の振動のみで声帯は存在しない", sum_points=0),
            Choice(question=q, text="鼻腔内の骨笛を鳴らしている", sum_points=0),
        ]
    )

    # --- Q15 ---
    q = Question(
        quiz=quiz,
        text="世界最大級のカエルとして知られる種はどれ？",
        order=order,
        multiple=False,
    )
    order += 1
    db.session.add(q)
    db.session.flush()
    db.session.add_all(
        [
            Choice(question=q, text="ゴライアスガエル", sum_points=1),
            Choice(question=q, text="コロブリカエル", sum_points=0),
            Choice(question=q, text="ヒメアマガエル", sum_points=0),
        ]
    )

    # ===== 判定（合否2段階） =====
    r_pass = Result(
        quiz=quiz,
        title="合格！カエル博士",
        description=(
            "おめでとうございます！\n"
            "高度でマニアックな内容を見事にクリア。あなたは立派なカエル博士です。"
        ),
        min_total=12,
        max_total=9999,
    )
    r_fail = Result(
        quiz=quiz,
        title="不合格…まだ道半ば",
        description=(
            "惜しい！上級問題は手強かったはず。\n"
            "生態・形態・行動の各分野を復習して再挑戦してみましょう。"
        ),
        min_total=-9999,
        max_total=11,
    )

    db.session.add_all([r_pass, r_fail])
    db.session.commit()
    print("[seed] カエル最上級テストを投入しました。")


# 直接実行用
if __name__ == "__main__":
    seed(db_uri_print=True)
