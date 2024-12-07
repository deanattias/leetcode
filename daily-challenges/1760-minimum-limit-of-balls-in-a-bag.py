from math import ceil

def minimumSize(nums: list[int], maxOperations: int) -> int:
        # Binary search appraoch

        def can_divide(max_balls):
            ops = 0
            for n in nums:
                ops += ceil(n / max_balls) - 1
                if ops > maxOperations:
                    return False
            return True

        # O(n * logm)
        left, right = 1, max(nums)
        while left < right:
            mid = left + ((right - left) // 2)
            if can_divide(mid):
                right = mid
            else:
                left = mid + 1
        return left

test_1 = minimumSize([9], 2)
test_2 = minimumSize([2,4,8,2], 4)

print(test_1)
print(test_2)
