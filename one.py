def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount %= coin
    return result

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    used_coins = {coin: 0 for coin in coins}

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coins[coin] += 1

    return used_coins

# Тестування функцій
amount = 113
print("Жадібний алгоритм:", find_coins_greedy(amount))
print("Алгоритм динамічного програмування:", find_min_coins(amount))
import time

# Функція для вимірювання часу виконання
def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

amount = 10**6  # велика сума

time_greedy = measure_time(find_coins_greedy, amount)
time_dynamic = measure_time(find_min_coins, amount)

print("Час виконання жадібного алгоритму:", time_greedy)
print("Час виконання алгоритму динамічного програмування:", time_dynamic)