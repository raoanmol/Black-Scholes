import yfinance as yf
import numpy as np

def fetch_financial_data(ticker):
    stock = yf.Ticker(ticker)
    
    try:
        # Get current stock info
        stock_info = stock.info
        # Try different fields for price retrieval
        current_price = stock_info.get('regularMarketPrice') or stock_info.get('preMarketPrice') or stock_info.get('postMarketPrice')

        if current_price is None:
            print("Current price is unavailable.")
            return

        # Calculate an example strike price as 105% of the current price
        strike_price = current_price * 1.05

        # Calculate implied volatility (simplified model, not real-world accurate)
        volatility = np.std(stock.history(period="1y")['Close'].pct_change()) * np.sqrt(252) * 100
        
        dividend_yield = stock_info.get('dividendYield', 0) * 100 if stock_info.get('dividendYield') is not None else 'N/A'
        
        # Getting the 10-year Treasury yield as an approximation for the risk-free rate
        treasury_ticker = "^TNX"  # Ticker for the 10-year Treasury Note yield
        treasury = yf.Ticker(treasury_ticker)
        treasury_data = treasury.history(period="1d")
        risk_free_rate = treasury_data['Close'].iloc[-1] if not treasury_data.empty else 'N/A'
        
        print(f"Ticker: {ticker}")
        print(f"Current Stock Price: ${current_price:.2f}")
        print(f"Strike Price: ${strike_price:.2f}")
        print(f"Dividend Yield: {dividend_yield:.2f}%")
        print(f"Volatility: {volatility:.2f}%")
        print(f"Current 10-Year Treasury Yield (Risk-Free Rate): {risk_free_rate:.2f}%")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ticker_symbol = input("Enter the stock ticker symbol: ")
    fetch_financial_data(ticker_symbol)
