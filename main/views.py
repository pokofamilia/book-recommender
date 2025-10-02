from django.shortcuts import render
from .forms import RecommendForm
from .utils import search_books, GENRE_MAP

def recommend_view(request):
    recommendations = []

    if request.method == "POST":
        form = RecommendForm(request.POST)
        if form.is_valid():
            print("フォーム送信されました！")
            print("フォームが有効です！")

            mood = form.cleaned_data["mood"]
            genre = form.cleaned_data["genre"]
            length = form.cleaned_data["length"]

            # --- 日本語マッピング ---
            mood_map = {
                "fun": "楽しい",
                "learn": "勉強",
                "relax": "リラックス",
            }

            length_map = {
                "short": "短編",
                "medium": "中編",
                "long": "長編"
            }

            # 英語ジャンルを日本語に変換
            query_genre = GENRE_MAP.get(genre, genre)

            # クエリを日本語で作る
            query = query_genre
            print("検索クエリ（テスト）:", query)

            # Google Books API で検索
            recommendations = search_books(query)
            print("検索結果:", recommendations)

    else:
        form = RecommendForm()

    return render(request, "main/recommend.html", {
        "form": form,
        "recommendations": recommendations,
    })
