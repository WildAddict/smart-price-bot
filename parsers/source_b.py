import aiohttp

async def fetch_source_b(query: str):
    """Парсинг второго источника (например, магазин Б)"""
    url = f"https://httpbin.org/get?search={query}"
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    return {
                        "title": f"Товар '{query}' в Магазине Б",
                        "price": 20000,
                        "url": "https://store-b.com/item"
                    }
        except Exception as e:
            print(f"Ошибка парсинга Источника Б: {e}")
    return None