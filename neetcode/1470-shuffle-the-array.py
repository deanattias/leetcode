def shuffle(nums: list[int], n: int) -> list[int]:
    # arr_x = nums[:n]
    # arr_y = nums[n:]
    # result = []
    # for i in range(len(nums) // 2):
    #     result.append(arr_x[i])
    #     result.append(arr_y[i])
    # return result

    # Pythonic approach
    return [val for pair in zip(nums[:n], nums[n:]) for val in pair]
