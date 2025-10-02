from django import forms

class RecommendForm(forms.Form):
    mood = forms.ChoiceField(
        choices=[
            ("fun", "楽しい気分"),
            ("learn", "勉強したい"),
            ("relax", "リラックスしたい"),
        ],
        label="今の気分は？"
    )

    genre = forms.ChoiceField(
        choices=[
            ("novel", "小説"),
            ("business", "ビジネス"),
            ("science", "科学"),
            ("history", "歴史"),
            ("fantasy", "ファンタジー"),
        ],
        label="ジャンルを選んでください"
    )

    length = forms.ChoiceField(
        choices=[
            ("short", "短い本（200ページ以下）"),
            ("medium", "中くらい（200〜400ページ）"),
            ("long", "長編（400ページ以上）")
        ],
        label="読みたい本の長さ"
    )
