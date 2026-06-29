import aiohttp
from bs4 import BeautifulSoup
import urllib.parse

async def fetch_source_a(query: str):
    """Реальный парсинг книжного каталога без защиты от ботов."""
    encoded_query = urllib.parse.quote(query)
    url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    async with aiohttp.ClientSession(headers=headers) as session:
        try:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, "html.parser")
                    
                    books = soup.find_all("article", class_="product_pod")
                    
                    for book in books:
                        title = book.h3.a["title"]
                        
                        if query.lower() in title.lower():
                            price_text = book.find("p", class_="price_color").text
                            price = float(price_text.replace("£", "").replace("Â", ""))
                            
                            relative_url = book.h3.a["href"].replace("../../../", "")
                            full_url = f"https://books.toscrape.com/catalogue/{relative_url}"
                            
                            return {
                                "title": f"Книга: {title} (Источник А)",
                                "price": int(price * 100),
                                "url": full_url
                            }
        except Exception as e:
            print(f"Ошибка реального парсинга: {e}")
            
    return {
        "title": f"Ничего не нашлось на реальном сайте по запросу '{query}'",
        "price": 9999,
        "url": "https://books.toscrape.com"
    }