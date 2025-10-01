# main/views.py
from django.shortcuts import render
from .forms import QuestionForm
from .utils import search_books

def recommend_view(request):
    recommendations = []

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            mood = form.cleaned_data["mood"]

            # mood に応じて日本語キーワードで検索
            if mood == "fun":
                query = "小説"
            elif mood == "learn":
                query = "ビジネス書"
            elif mood == "relax":
                query = "エッセイ"
            else:
                query = "本"

            recommendations = search_books(query)
            print(recommendations)  # デバッグ用

    else:
        form = QuestionForm()

    return render(request, "main/recommend.html", {
        "form": form,
        "recommendations": recommendations
    })
