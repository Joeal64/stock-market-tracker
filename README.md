# Stock Market Tracker

A Python stock tracker with Telegram bot. Type a company name to get stock price and chart.

## Features

- Get real-time stock prices
- Generate 1-month price charts  
- Telegram bot integration
- Automatic company name to symbol lookup

## Installation

Install dependencies:
```bash
pip install yfinance yahooquery matplotlib python-telegram-bot
```

## Usage

### 1. Get Stock Price
```bash
python fetch_stock.py
```
Enter company name when prompted.

### 2. Plot Stock Chart
```bash
python plot_stock.py
```
Enter company name to see price chart.

### 3. Telegram Bot

1. Get bot token from [@BotFather](https://t.me/botfather)
2. Replace token in `telegram_bot.py`
3. Run bot:
   ```bash
   python telegram_bot.py
   ```

**Bot Commands:**
- `/start` - Get started
- `/stock <company_name>` - Get price and chart

**Example:** `/stock Apple`

## Files

- `fetch_stock.py` - Get stock prices
- `plot_stock.py` - Generate charts
- `telegram_bot.py` - Telegram bot

## License

MIT
