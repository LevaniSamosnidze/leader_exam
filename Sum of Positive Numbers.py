# Problem 1: Sum of Positive Numbers - 2ქ
# Challenge:
#  Create a function that takes a list of numbers and returns the sum of all positive numbers.
# Instructions:
# Input: A list of integers (e.g., [1, -4, 7, 12]).
# Output: The sum of all positive integers in the list.
# Test Cases:
# assert problem_1_sum_of_positive([1, -4, 7, 12]) == 20
# assert problem_1_sum_of_positive([-1, -2, -3, -4]) == 0
# assert problem_1_sum_of_positive([]) == 0


def position_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
        else:
            continue
    if arr == []:
        return 0
    return sum

print(position_sum([1, -4, 7, 12]))