# Problem 4: Longest Substring Without Repeating Characters - 5ქ
# Challenge:
#  Create a function that finds the length of the longest substring without repeating characters.
# Instructions:
# Input: A string (e.g., "abcabcbb").
# Output: An integer representing the length of the longest substring (e.g., 3 for "abc").
# Test Cases:
# assert longest_unique_substring("abcabcbb") == 3
# assert longest_unique_substring("bbbbb") == 1
# assert longest_unique_substring("") == 0
# assert longest_unique_substring("pwwkew") == 3


def find_repeating_characters(word):
    s = set()
    for i in word:
        if word.count(i) > 1:
            s.add(i)

    return len(s)

print(find_repeating_characters("abcabcbb"))