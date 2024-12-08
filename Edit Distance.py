# Problem 10: Edit Distance - 10ქ
# Challenge:
#  Given two strings word1 and word2, find the minimum number of operations required to convert
#  word1 into word2. You have three operations allowed: insertion, deletion, or substitution.
# Instructions:
# Input: Two strings word1 and word2 (e.g., "horse", "ros").
# Output: The minimum number of operations required to convert word1 into word2.
# Test Cases:
# assert min_distance("horse", "ros") == 3
# assert min_distance("intention", "execution") == 5
# assert min_distance("kitten", "sitting") == 3

def distance(s1, s2):
    counter = 0
    count1 = 0
    count2 = 0

    while count1 < len(s1) or count2 < len(s2):
        if count1 < len(s1) and count2 < len(s2) and s1[count1] == s2[count2]:
            count1 += 1
            count2 += 1
        else:
            counter += 1
            if count1 == len(s1):
                count2 += 1
            elif count2 == len(s2):
                count1 += 1
            else:
                count1 += 1
                count2 += 1

    return counter

print(distance("intention", "execution"))