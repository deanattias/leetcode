def removeElement(nums: list[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


test_1 = removeElement([3,2,2,3],3)
test_2 = removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)


assert  test_1 == 2
assert test_2 == 5

