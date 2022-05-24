"""
Given the stock_prices as an input array find the best time to have purchased the stocks.
"""

def max_profit_brute_force(stock_prices):
    """
    Brute force approach to get the max profit
    O(n^2)
    """
    price_count = len(stock_prices)
    max_profit = float('-inf')
    buy = sell = 0
    for i in range(price_count):
        local_sum = 0
        for j in range(i, price_count):
            local_sum += stock_prices[j]
            if local_sum > max_profit:
                buy = i
                sell = j
                max_profit = local_sum
        print(f"[max_profit_brute_force] The local sum is :: {local_sum} on day [{i}]")
    return buy, sell, max_profit


if __name__ == "__main__":
    stock_prices = [13, -3, -25, 20,-3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    buy, sell, profit = max_profit_brute_force(stock_prices)
    print(f"[main] The computed best time to buy, sell and profit is ::" 
          f"buy @{buy}-> [{stock_prices[buy]}]"
          f"sell@{sell}-> [{stock_prices[sell]}]"
          f"profit{profit}"
          )
