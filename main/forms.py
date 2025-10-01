from django import forms

class QuestionForm(forms.Form):
    mood = forms.ChoiceField(
        choices=[
            ("fun", "楽しい気分になりたい"),
            ("learn", "学びたい"),
            ("relax", "リラックスしたい"),
        ],
        label="今の気分は？"
    )
    length = forms.ChoiceField(
        choices=[
            ("short", "短くサクッと読める本"),
            ("long", "じっくり読める長編"),
        ],
        label="どんな長さの本を読みたい？"
    )
