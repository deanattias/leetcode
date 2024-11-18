def merge_alternately(word1: str, word2: str) -> str:
    # Use a list to store interleaved characters
    result = []

    # Interleave characters until one string is exhausted
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1

    # Add remaining characters from the longer string
    result.extend(word1[i:])
    result.extend(word2[j:])

    # Return the merged string
    return ''.join(result)
