from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RecommendForm(forms.Form):
    mood = forms.CharField(label="気分", max_length=50, required=True)
    genre = forms.ChoiceField(
        label="ジャンル",
        choices=[
            ("novel", "小説"),
            ("business", "ビジネス"),
            ("science", "科学"),
            ("history", "歴史"),
            ("fantasy", "ファンタジー"),
        ],
        required=True,
    )
    length = forms.ChoiceField(
        label="長さ",
        choices=[
            ("short", "短編"),
            ("medium", "中編"),
            ("long", "長編"),
        ],
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Crispy Forms 用の設定
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "row g-3"
        self.helper.label_class = "col-form-label fw-bold"
        self.helper.field_class = "form-control"

        # 送信ボタンを追加
        self.helper.add_input(Submit("submit", "診断する", css_class="btn btn-primary w-100"))
