def knapsack_01_memo(weights, profit, capacity, n, memo):
    # Base case: no items or no capacity
    if n == 0 or capacity == 0:
        return 0

    # Check if result is already computed
    if memo[n][capacity] is not None:
        return memo[n][capacity]

    # If weight of the current item is more than the remaining capacity, don't include it
    if weights[n - 1] > capacity:
        memo[n][capacity] = knapsack_01_memo(weights, profit, capacity, n - 1, memo)
    else:
        # Take the maximum of including or not including the current item
        include_item = profit[n - 1] + knapsack_01_memo(weights, profit, capacity - weights[n - 1], n - 1, memo)
        exclude_item = knapsack_01_memo(weights, profit, capacity, n - 1, memo)
        memo[n][capacity] = max(include_item, exclude_item)

    return memo[n][capacity]

def knapsack_with_items(weights, profit, capacity):
    n = len(profit)
    memo = [[None] * (capacity + 1) for _ in range(n + 1)]  # Memoization table

    # Calculate maximum profit using memoized approach
    max_profit = knapsack_01_memo(weights, profit, capacity, n, memo)

    # Backtrack to find the included items
    w = capacity
    included_items = []
    for i in range(n, 0, -1):
        if memo[i][w] != memo[i - 1][w]:  # If the value is different, the item is included
            included_items.append(i - 1)  # Include the item (indexing starts from 0)
            w -= weights[i - 1]

    return max_profit, included_items

# Example usage 
if __name__ == "__main__": 
    profit = [int(i) for i in input("Enter Profit of elements - ").split()] 
    weights = [int(i) for i in input("Enter Weight of elements - ").split()] 
    capacity = int(input("Enter Total Capacity of Knapsack - ")) 

    max_value, included_items = knapsack_with_items(weights, profit, capacity) 
    print(f"Maximum Profit: {max_value}") 

    print("Items included:")
    for i in included_items:
        # Items are 1-indexed in the output for user-friendly output
        print(f"Item No. {i+1} with Weight = {weights[i]} and Profit = {profit[i]}")
