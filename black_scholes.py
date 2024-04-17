import math
from scipy.stats import norm

def black_scholes(S, K, T, r, q, sigma):
    # S: stock price
    # K: strike price
    # T: time to maturity
    # r: risk-free rate (as a decimal)
    # q: dividend yield (as a decimal)
    # sigma: volatility (as a decimal)
    
    # Calculate d1 and d2 parameters
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    # Calculate the call price
    call_price = S * math.exp(-q * T) * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    
    # Calculate the put price using put-call parity
    put_price = call_price + K * math.exp(-r * T) - S * math.exp(-q * T)
    
    return call_price, put_price

def main():
    print("Black-Scholes Option Price Calculator")
    
    S = float(input("Enter the current stock price (USD): "))
    K = float(input("Enter the strike price (USD): "))
    T = float(input("Enter the time to maturity (years): "))
    q = float(input("Enter the dividend yield (%): ")) / 100
    sigma = float(input("Enter the volatility (%): ")) / 100
    r = float(input("Enter the risk-free interest rate (%): ")) / 100
    
    call_price, put_price = black_scholes(S, K, T, r, q, sigma)
    
    print(f"Call Option Price: ${call_price:.2f}")
    print(f"Put Option Price: ${put_price:.2f}")

if __name__ == "__main__":
    main()
