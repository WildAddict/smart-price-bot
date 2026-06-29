import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv

from parsers.source_a import fetch_source_a
from parsers.source_b import fetch_source_b

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот-сравнитель цен.\n"
        "Отправь мне название товара, а я найду самое выгодное предложение!"
    )

@dp.message(F.text)
async def handle_search(message: Message):
    query = message.text
    waiting_msg = await message.answer(f"🔍 Ищу '{query}' по всем источникам, подождите...")

    results = await asyncio.gather(
        fetch_source_a(query),
        fetch_source_b(query),
        return_exceptions=True
    )

    valid_results = [r for r in results if r and not isinstance(r, Exception)]

    if not valid_results:
        await waiting_msg.edit_text("❌ Ничего не найдено или произошла ошибка поиска.")
        return

    valid_results.sort(key=lambda x: x["price"])
    best_offer = valid_results[0]

    response_text = (
        f"✅ **Самое выгодное предложение найденно!**\n\n"
        f"📦 **Товар:** {best_offer['title']}\n"
        f"💰 **Цена:** {best_offer['price']} руб.\n"
        f"🔗 **Ссылка:** [Перейти к покупке]({best_offer['url']})\n\n"
        f" Всего проверено источников: {len(valid_results)}"
    )

    await waiting_msg.edit_text(response_text, parse_mode="Markdown", disable_web_page_preview=True)

async def main():
    print("Бот успешно запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())