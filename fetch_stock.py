from yahooquery import search
import yfinance as yf

def get_stock_symbol(company_name):
    search_result = search(company_name)  # Use yahooquery's search function
    if search_result and "quotes" in search_result and search_result["quotes"]:
        return search_result["quotes"][0]["symbol"]  # Get the first matching symbol
    return None  # If no match, return None

def fetch_stock_price(symbol):
    stock = yf.Ticker(symbol)
    stock_info = stock.history(period="1d")
    price = stock_info['Close'].iloc[0]
    return price

if __name__ == "__main__":
    company_name = input("Enter company name (e.g., Apple): ")
    symbol = get_stock_symbol(company_name)

    if symbol:
        price = fetch_stock_price(symbol)
        print(f"The current price of {company_name} ({symbol}) is: ${price}")
    else:
        print(f"Could not find a stock symbol for '{company_name}'. Try again.")
