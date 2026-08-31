# Making Change Problem using Dynamic Programming

print("=" * 60)
print("MAKING CHANGE PROBLEM")
print("USING DYNAMIC PROGRAMMING")
print("=" * 60)

n = int(input("Enter number of coin denominations: "))

coins = []

for i in range(n):
    coin = int(input(f"Enter value of coin {i + 1}: "))
    coins.append(coin)

amount = int(input("Enter amount to make: "))

# DP array
dp = [float("inf")] * (amount + 1)
used_coin = [-1] * (amount + 1)

dp[0] = 0

# Dynamic Programming
for current_amount in range(1, amount + 1):
    for coin in coins:
        if coin <= current_amount:
            if dp[current_amount - coin] + 1 < dp[current_amount]:
                dp[current_amount] = dp[current_amount - coin] + 1
                used_coin[current_amount] = coin

print("\n" + "=" * 60)
print("RESULT")
print("=" * 60)

if dp[amount] == float("inf"):
    print("Change cannot be made for the given amount.")
else:
    print("Minimum number of coins:", dp[amount])

    selected_coins = []
    current = amount

    while current > 0:
        coin = used_coin[current]
        selected_coins.append(coin)
        current -= coin

    print("Coins used:", selected_coins)

print("\nTime Complexity: O(n × amount)")
print("Space Complexity: O(amount)")

print("=" * 60)