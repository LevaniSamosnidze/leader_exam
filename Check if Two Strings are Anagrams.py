# Problem 5: Check if Two Strings are Anagrams - 5ქ
# Challenge:
#  Write a function to check if two strings are anagrams (contain the same characters in the same frequency).
# Instructions:
# Input: Two strings (e.g., "listen" and "silent").
# Output: A boolean (True or False) indicating if the strings are anagrams.
# Test Cases:
# assert are_anagrams("listen", "silent") == True
# assert are_anagrams("hello", "world") == False
# assert are_anagrams("triangle", "integral") == True


def are_anagrams(str1, str2):
    s1 = sorted(str1)
    s2 = sorted(str2)
    for i in range(len(str1)):
        if s1[i] == s2[i]:
            return True
        else:
            return False
        
print(are_anagrams("triangle", "integral"))