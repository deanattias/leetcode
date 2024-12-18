from collections import deque


def finalPrices(prices: list[int]) -> list[int]:
    # # Approach 1: Brute force approach

    # # Create a copy of original prices array to store discounted prices
    # result = prices.copy()

    # for i in range(len(prices)):
    #     # Look for first smaller or equal price that comes after the current item
    #     for j in range(i + 1, len(prices)):
    #         if prices[j] <= prices[i]:
    #             # Apply discount by subtracting prices[j] from current price
    #             result[i] = prices[i] - prices[j]
    #             break

    # return result

    # Approach 2: Monotonic Stack Approach
    # Create a copy of prices array to store discounted prices
    result = prices.copy()

    stack = deque()

    for i in range(len(prices)):
        # Process items that can be discounted by current price
        while stack and prices[stack[-1]] >= prices[i]:
            # Apply discount to previous item using current price
            result[stack.pop()] -= prices[i]
        # ADd current index to stack
        stack.append(i)

    return result
