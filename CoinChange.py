
# Output Format

# Print a long integer denoting the number of ways we can get a sum of  from the given infinite supply of  types of coins.

# Sample Input 0

# 4 3
# 1 2 3
# Sample Output 0

# 4
# Explanation 0

# Given coins of denominations [1, 2, 3] and a target amount of 4, the following 4 sets of coins meet the goal: 
# [1, 1, 1, 1], [1, 1, 2], [2, 2] and [1, 3].



# target, array of coins
def getWays(n, c): 
    l = []
    for i in c
        p = 0
        p = i
 
    counts = [1] + [0] * 3

def coinChange(n, coins):
    #print coins, n
    counts = [1] + [0] * n
    for c in coins:
        for i in range(len(counts)):
            if c + i <= n:
                counts[i + c] += counts[i]
    return counts[-1]

print coinChange(n, coins)