import time

# List of coin denominations
COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}
    for coin in COINS:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount):
    # Initialize the dynamic programming table
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    # Track the coins used
    coin_used = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in COINS:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    # Backtrack to find the coins used
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

def compare_performance(amount):
    start = time.time()
    greedy_result = find_coins_greedy(amount)
    end = time.time()
    greedy_time = end - start
    
    start = time.time()
    dp_result = find_min_coins(amount)
    end = time.time()
    dp_time = end - start
    
    print(f"Greedy Algorithm for {amount}: {greedy_result} (Time: {greedy_time:.6f} seconds)")
    print(f"Dynamic Programming for {amount}: {dp_result} (Time: {dp_time:.6f} seconds)")

# Example usage
amount = 113
print("Greedy Algorithm:", find_coins_greedy(amount))
print("Dynamic Programming:", find_min_coins(amount))

# Compare performance for a large amount
compare_performance(10000)
