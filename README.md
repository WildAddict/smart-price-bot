# SmartPrice | Asynchronous Telegram Bot for Price Comparison

An asynchronous Telegram bot built with **aiogram 3**. The bot allows users to find and compare product prices in real time across multiple independent sources.

## 🚀 Features

* **Parallel source polling:** Uses asynchronous processing to collect data from multiple modules simultaneously.
* **Live web scraping:** Includes a working online store parser built with the `BeautifulSoup4` library.
* **Smart sorting:** Automatically compares offers and shows users the best available option, with a direct link to the product.
* **Secure configuration:** Sensitive data and API tokens are stored in environment variables.

## 🛠 Tech Stack

* **Language:** Python 3.11+
* **Bot framework:** `aiogram` (v3)
* **Asynchronous HTTP requests:** `aiohttp`
* **Web scraping:** `beautifulsoup4`
* **Configuration management:** `python-dotenv`

## 📦 Project Structure

* `bot.py` — the main entry point, containing the bot dispatcher and handlers.
* `parsers/` — a package containing separate parser modules.
  * `__init__.py` — Python package marker.
  * `source_a.py` — module for parsing live HTML pages from a product catalog.
  * `source_b.py` — mock module used to simulate product pricing.
* `.env` — configuration file containing tokens and other environment variables (not included in the repository).
* `requirements.txt` — list of project dependencies.

## 🔧 Local Setup

1. Clone the repository.
2. Create and activate a virtual environment named `venv`.
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```
