# Problem 8: Longest Consecutive Sequence - 8ქ
# Challenge:
#  Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Instructions:
# Input: A list of integers (e.g., [100, 4, 200, 1, 3, 2]).
# Output: The length of the longest consecutive sequence (e.g., 4).
# Test Cases:
# assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4  # [1, 2, 3, 4]
# assert longest_consecutive([0, 0]) == 1
# assert longest_consecutive([9, 1, 4, 7, 3, 2, 8, 5, 6]) == 9


def longest_consecutive(nums):
    if not nums:
        return 0
    
    s = set(nums)
    len1 = 0
    
    for i in s:
        if i - 1 not in s:
            count1 = i
            count2 = 1
            
            while count1 + 1 in s:
                count1 += 1
                count2 += 1
            
            len1 = max(len1, count2)
    
    return len1

print(longest_consecutive([9, 1, 4, 7, 3, 2, 8, 5, 6]))