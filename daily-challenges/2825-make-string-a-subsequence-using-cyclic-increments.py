def canMakeSubsequence(str1: str, str2: str) -> bool:
    # Initialize two pointers
    i, j = 0, 0
    n, m = len(str1), len(str2)

    while i < n and j < m:
        # Check if characters match or can match after a cyclic increment
        if str1[i] == str2[j] or chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
            j += 1  # Move the pointer in str2 as there's a match
        i += 1  # Always move the pointer in str1

    # If we processed all characters in str2, it is a subsequence
    return j == m
