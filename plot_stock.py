from yahooquery import search
import yfinance as yf
import matplotlib.pyplot as plt

def get_stock_symbol(company_name):
    search_result = search(company_name)  # Use yahooquery to find stock symbol
    if search_result and "quotes" in search_result and search_result["quotes"]:
        return search_result["quotes"][0]["symbol"]  # Get the first matching symbol
    return None  # If no match, return None

def plot_stock(symbol):
    stock = yf.Ticker(symbol)
    history = stock.history(period="1mo")  # Fetch last month's stock data

    plt.figure(figsize=(10, 5))
    plt.plot(history.index, history['Close'], label=f"{symbol} Price")
    
    plt.xlabel("Date")
    plt.ylabel("Stock Price (USD)")
    plt.title(f"{symbol} Stock Price Trend")
    plt.legend()
    plt.grid()
    
    plt.show()

if __name__ == "__main__":
    company_name = input("Enter company name (e.g., Apple): ")
    symbol = get_stock_symbol(company_name)

    if symbol:
        plot_stock(symbol)
    else:
        print(f"Could not find a stock symbol for '{company_name}'. Try again.")
