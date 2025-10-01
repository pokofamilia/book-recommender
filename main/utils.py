# main/utils.py
import requests

def search_books(query, max_results=5):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query,
        "maxResults": max_results,
        # "key": "YOUR_API_KEY"  # 必要ならここに APIキー
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        books = []
        for item in data.get("items", []):
            info = item.get("volumeInfo", {})
            books.append({
                "title": info.get("title", "タイトルなし"),
                "authors": ", ".join(info.get("authors", ["不明"])),
                "description": info.get("description", "説明なし"),
                "thumbnail": info.get("imageLinks", {}).get("thumbnail", "")
            })
        return books
    else:
        print("Error:", response.status_code)
        return []
