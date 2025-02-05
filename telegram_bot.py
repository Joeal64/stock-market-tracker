import logging
import yfinance as yf
from yahooquery import search
import matplotlib.pyplot as plt
import io
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

#Bot Username is Stock_64Bot
TELEGRAM_BOT_TOKEN = "7546685006:AAFFRjgQQ3iSVnjCjcb2U3BysKYGK1sAbio"

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def get_stock_symbol(company_name):
    """Fetch the stock symbol for a given company name"""
    search_result = search(company_name)
    if search_result and "quotes" in search_result and search_result["quotes"]:
        return search_result["quotes"][0]["symbol"]
    return None

def fetch_stock_price(symbol):
    """Fetch the latest stock price for a given symbol"""
    stock = yf.Ticker(symbol)
    stock_info = stock.history(period="1d")
    if not stock_info.empty:
        return stock_info['Close'].iloc[0]
    return None

def plot_stock(symbol):
    """Generate a stock price plot and return as an image"""
    stock = yf.Ticker(symbol)
    history = stock.history(period="1mo")  # Fetch last month's stock data

    plt.figure(figsize=(10, 5))
    plt.plot(history.index, history['Close'], label=f"{symbol} Price", color="blue")
    
    plt.xlabel("Date")
    plt.ylabel("Stock Price (USD)")
    plt.title(f"{symbol} Stock Price Trend")
    plt.legend()
    plt.grid()

    # Save plot to a BytesIO object
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format="png")
    plt.close()
    image_stream.seek(0)  # Move to the beginning of the stream

    return image_stream  # Return the image for sending

async def stock(update: Update, context: CallbackContext) -> None:
    """Handle /stock command to get stock price and chart"""
    if not context.args:
        await update.message.reply_text("Usage: /stock <company_name>")
        return

    company_name = " ".join(context.args)
    symbol = get_stock_symbol(company_name)

    if symbol:
        price = fetch_stock_price(symbol)
        if price:
            await update.message.reply_text(f"The current price of {company_name} ({symbol}) is: ${price:.2f}")

            # Generate stock plot
            image_stream = plot_stock(symbol)
            await update.message.reply_photo(photo=image_stream, caption=f"{company_name} ({symbol}) Stock Price Chart 📊")
        else:
            await update.message.reply_text(f"Could not retrieve price data for {symbol}.")
    else:
        await update.message.reply_text(f"Could not find a stock symbol for '{company_name}'.")

async def start(update: Update, context: CallbackContext) -> None:
    """Start command"""
    await update.message.reply_text("Hello! Send /stock <company_name> to get the latest stock price and a trend chart.")

def main():
    """Main function to start the bot"""
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stock", stock))

    # Start the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
