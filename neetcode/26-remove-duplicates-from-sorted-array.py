def removeDuplicates(self, nums: list[int]) -> int:
    left = 1

    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    return left

