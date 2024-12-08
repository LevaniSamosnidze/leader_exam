# Problem 3: Find the Missing Number - 2ქ
# Challenge:
#  Create a function to find the missing number in a list of integers from 1 to n.
# Instructions:
# Input: A list of integers from 1 to n with one number missing (e.g., [1, 2, 4, 5]).
# Output: The missing number (e.g., 3 in this case).
# Test Cases:
# assert find_missing_number([1, 2, 4, 5]) == 3
# assert find_missing_number([3, 5, 6, 1, 2]) == 4
# assert find_missing_number([2]) == 1

def find_num(arr):
    if not arr:
        return 1
    
    arr_set = set(arr)
    
    num = 1
    while num in arr_set:
        num += 1
    
    return num
    
print(find_num([3, 5, 6, 1, 2])) 
