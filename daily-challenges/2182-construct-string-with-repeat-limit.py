from collections import Counter
from heapq import heapify, heappop, heappush


def repeatLimitedString(s: str, repeatLimit: int) -> str:
    # # Approach 1: Greedy Character Frequency Distribution
    # freq = [0] * 26
    # for char in s:
    #     freq[ord(char) - ord("a")] += 1

    # result = []
    # current_char_index = 25  # Start from the largest character
    # while current_char_index >= 0:
    #     if freq[current_char_index] == 0:
    #         current_char_index -= 1
    #         continue

    #     use = min(freq[current_char_index], repeatLimit)
    #     result.append(chr(current_char_index + ord("a")) * use)
    #     freq[current_char_index] -= use

    #     if freq[current_char_index ] > 0:  # Need to add a smaller character
    #         smaller_char_index = current_char_index - 1
    #         while smaller_char_index >= 0 and freq[smaller_char_index] == 0:
    #             smaller_char_index -= 1
    #         if smaller_char_index < 0:
    #             break
    #         result.append(chr(smaller_char_index + ord("a")))
    #         freq[smaller_char_index] -= 1

    # return "".join(result)

    # Approach 2: Heap-Optimized Greedy Character Frequency Distribution
    max_heap = [(-ord(c), cnt) for c, cnt, in Counter(s).items()]
    heapify(max_heap)
    result = []

    while max_heap:
        char_neg, count = heappop(max_heap)
        char = chr(-char_neg)
        use = min(count, repeatLimit)
        result.append(char * use)

        if count > use and max_heap:
            next_char_neg, next_count = heappop(max_heap)
            result.append(chr(-next_char_neg))
            if next_count > 1:
                heappush(max_heap, (next_char_neg, next_count - 1))
            heappush(max_heap, (char_neg, count - use))

    return "".join(result)