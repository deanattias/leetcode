def maxCount(banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        max_count, current_sum = 0, 0

        for i in range(1, n + 1):
            if i not in banned_set:
                current_sum += i
                if current_sum > maxSum:
                    break
                max_count += 1

        return max_count
