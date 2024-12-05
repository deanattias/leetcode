def canChange(start: str, target: str) -> bool:
    # Initialize points for start and target strings
    i, j = 0, 0
    n = len(start)

    while i < n or j < n:
        # Skip blank spaces ('_') in both strings
        while i < n and start[i] == '_':
            i += 1
        while j < n and target[j] == '_':
            j += 1

        # If one pointer reaches the end, both must reach the end
        if i == n or j == n:
            return i == j

        # The characters at the current position must match
        if start[i] != target[j]:
            return False

        # Validate movement rules
        if start[i] == 'L' and i < j:  # 'L' can't move right
            return False
        if start[i] == 'R' and i > j:  # 'R' can't move left
            return False

        # Move to the next piece
        i += 1
        j += 1

    return True
