def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    arr = sentence.split()
    for i in range(len(arr)):
        if searchWord in arr[i][:len(searchWord)]:
            return i + 1
    return -1


test_1 = isPrefixOfWord("i love eating burger", "burg")
test_2 = isPrefixOfWord("this problem is an easy problem", "pro")

assert test_1 == 4
assert test_2 == 2



