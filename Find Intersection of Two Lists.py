# roblem 6: Find Intersection of Two Lists - 5ქ
# Challenge:
#  Write a function to find the common elements between two lists.
# Instructions:
# Input: Two lists of integers (e.g., [1, 2, 3] and [2, 3, 4]).
# Output: A list of integers representing the intersection (e.g., [2, 3]).
# Test Cases:
# assert find_intersection([1, 2, 3], [2, 3, 4]) == [2, 3]
# assert find_intersection([1, 1, 2], [1, 3]) == [1]
# assert find_intersection([], [1, 2]) == []


def find_intersection(list1, list2):
    if list1 == [] or list2 == []:
        return []
    result = []
    s = set()
    for i in list1:
        if i in list2:
            s.add(i)
    for i in s:
        result.append(i)
    return result

print(find_intersection([1, 2, 3, 19, 3], [2, 19, 3, 4]))