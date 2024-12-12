import math


def pickGifts(gifts: list[int], k: int) -> int:
    while k:
        gifts = sorted(gifts)
        gifts[-1] = math.floor(math.sqrt(gifts[-1]))
        k -= 1
    return sum(gifts)


test_1 = pickGifts([25,64,9,4,100], 4)
test_2 = pickGifts([1,1,1,1], 4)

assert test_1 == 29
assert test_2 == 4
