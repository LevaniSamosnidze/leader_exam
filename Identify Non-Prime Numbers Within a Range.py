# Problem 9: Identify Non-Prime Numbers Within a Range
#  Objective:
#  Create a function that accepts two integers, start and end, and returns a list of all non-prime numbers within the range [start, end] (inclusive). A non-prime number is defined as any integer greater than 1 that is not a prime number.
# Example Test Cases:
# Input: start = 10, end = 20
#  Output: [10, 12, 14, 15, 16, 18, 20]
# Input: start = 1, end = 10
#  Output: [1, 4, 6, 8, 9, 10]
# Input: start = 20, end = 30
#  Output: [20, 21, 22, 24, 25, 26, 27, 28, 30]
# Input: start = 24, end = 25
#  Output: [24, 25]
# Input: start = 1, end = 1
#  Output: [1]


def primes(start, end):
    res = []

    for i in range(start, end + 1):
        if i == 1:
            res.append(i)
        else:
            prime = True
            for x in range(2, int(i ** 0.5) + 1):
                if i % x == 0:
                    prime = False
                    break
            if not prime:
                res.append(i)

    return res

print(primes(10, 20))  
 


