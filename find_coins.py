import time

def find_coins_greedy(items, capacity):

    start_time = time.time()
    n = 0
    value = []
    count_dict = {}
    
    while sum(value) != capacity and n < len(items):
        if capacity >= items[n]:
            value.append(items[n])
            capacity -= items[n]
        else:
            n += 1
    
    for val in value:
        if val not in count_dict:
            count_dict[val] = 1
        else:
            count_dict[val] += 1
    
    end_time = time.time()
    return count_dict, end_time - start_time

def find_min_coins(coins, amount):

    start_time = time.time()
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    coin_counts = {}
    remaining = amount
    while remaining > 0:
        coin = coin_used[remaining]
        coin_counts[coin] = coin_counts.get(coin, 0) + 1
        remaining -= coin

    end_time = time.time()
    return coin_counts, end_time - start_time

coinsS = [50, 25, 10, 5, 2, 1]
moneyS = 113

result_greedyS, time_greedyS = find_coins_greedy(coinsS, moneyS)
result_min_coinsS, time_min_coinsS = find_min_coins(coinsS, moneyS)

coinsB = [50, 25, 10, 5, 2, 1]
moneyB = 165345

result_greedyB, time_greedyB = find_coins_greedy(coinsB, moneyB)
result_min_coinsB, time_min_coinsB = find_min_coins(coinsB, moneyB)

print(f"|{'Algorithm':<35} | {'Time':<10} |")
print(f"|{'-'*35} | {'-'*10} |")
print(f"|{'Greedy (small number)':<35} | {time_greedyS:10.5f} |")
print(f"|{'Dynamic programming (small number)':<35} | {time_min_coinsS:10.5f} |")
print(f"|{'Greedy (large number)':<35} | {time_greedyB:10.5f} |")
print(f"|{'Dynamic programming (large number)':<35} | {time_min_coinsB:10.5f} |")

