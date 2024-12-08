def maxTwoEvents(events: list[list[int]]) -> int:
    # Step 1: Prepare the line sweep events
    line_sweep = []
    for start, end, val in events:
        line_sweep.append([start, 1, val])  # Event starts
        line_sweep.append([end + 1, -1, val])  # Event ends

    # Step 2: Sort events by time, and by type (-1 before 1 if same time)
    line_sweep.sort()

    # Step 3: Initialize tracking variables
    max_val = 0  # Maximum sum of two events
    max_seen = 0  # Best single event value seen so far

    # Step 4: Process the sorted events
    for point, status, val in line_sweep:
        if status == 1:  # Event starts
            max_val = max(max_val, max_seen + val)
        elif status == -1:  # Event ends
            max_seen = max(max_seen, val)

    # Step 5: Return the result
    return max_val


test_1 = maxTwoEvents([[1, 3, 2], [4, 5, 2], [2, 4, 3]])
test_2 = maxTwoEvents([[1, 3, 2], [4, 5, 2], [1, 5, 5]])
test_3 = maxTwoEvents([[1, 5, 3], [1, 5, 1], [6, 6, 5]])

assert test_1 == 4
assert test_2 == 5
assert test_3 == 8
