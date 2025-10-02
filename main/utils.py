import requests

GENRE_MAP = {
    "novel": "小説",
    "business": "ビジネス",
    "science": "科学",
    "history": "歴史",
    "fantasy": "ファンタジー",
}

def search_books(query, max_results=10):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": query, "maxResults": max_results}
    response = requests.get(url, params=params)

    data = response.json()
    print("APIレスポンス:", data)  # ←ここで中身を確認

    items = data.get("items", [])
    return [
        {
            "title": item["volumeInfo"].get("title", "タイトル不明"),
            "authors": ", ".join(item["volumeInfo"].get("authors", ["著者不明"])),
            "thumbnail": item["volumeInfo"].get("imageLinks", {}).get("thumbnail", ""),
        }
        for item in items
    ]
