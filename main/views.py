from django.shortcuts import render
from .forms import QuestionForm
from .models import Book

def recommend_view(request):
    recommendation = None

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            mood = form.cleaned_data["mood"]
            length = form.cleaned_data["length"]

            # 簡単なロジック例
            if mood == "fun":
                recommendation = Book.objects.filter(genre="小説").first()
            elif mood == "learn":
                recommendation = Book.objects.filter(genre="ビジネス").first()
            elif mood == "relax":
                recommendation = Book.objects.filter(genre="エッセイ").first()
    else:
        form = QuestionForm()

    return render(request, "main/recommend.html", {
        "form": form,
        "recommendation": recommendation
    })
