def knapsack_01(weights, profit, capacity):
    """
    Solves the 0/1 Knapsack Problem using dynamic programming.
    Parameters:
    weights (list): List of item weights.
    profit (list): List of item profit.
    capacity (int): Maximum weight capacity of the knapsack.
    Returns:
    tuple: A tuple containing:
           - Maximum value that can be achieved.
           - List of items included in the knapsack.
    """
    n = len(profit)  # Number of items
    # dp[i][w] will store the maximum value for the first i items with weight limit w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the dp table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + profit[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find the items included
    w = capacity
    included_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i - 1)  # Include the item (indexing starts from 0)
            w -= weights[i - 1]

    return dp[n][capacity], included_items

# Example usage
if __name__ == "__main__":
    #profit = [60, 100, 120]  # profit of items
    #weights = [10, 20, 30]  # Weights of items
    #capacity = 25  # Capacity of knapsack

    profit=[int(i) for i in input("Enter Profit of elements - ").split()]
    weights=[int(i) for i in input("Enter Weight of elements - ").split()]
    capacity=int(input("Enter Total Capacity of Knapsack - "))

    max_value, included_items = knapsack_01(weights, profit, capacity)
    print(f"Maximum Profit: {max_value}")
    included_items=[i+1 for i in included_items]
    print("Items included - ")
    for i in included_items:
        print("Item No. ",i," weight = ",weights[i])
        
