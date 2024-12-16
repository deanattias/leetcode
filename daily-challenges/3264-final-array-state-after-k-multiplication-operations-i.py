from heapq import heapify, heappop, heappush


def getFinalState(nums: list[int], k: int, multiplier: int) -> list[int]:
    # Naive approach
    # for _ in range(k):
    #     min_idx = nums.index(min(nums))
    #     nums[min_idx] *= multiplier
    # return nums

    # Optimized approach using min-heap
    # Create a min-heap with (value, index)
    min_heap = [(value, idx) for idx, value in enumerate(nums)]
    heapify(min_heap)

    for _ in range(k):
        # Get the smallest element
        value, idx = heappop(min_heap)
        # Update its value
        nums[idx] = value * multiplier
        # Push the updated value back into the heap
        heappush(min_heap, (nums[idx], idx))

    return nums

