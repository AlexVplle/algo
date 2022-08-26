def karatsuba(x, y):
    """Complexity : O(n**1.585) instead of O(n**2)"""
    negative = 1
    if x < 0 :
        negative *= -1
    if y < 0 :
        negative *= -1
    x, y = abs(x), abs(y)
    if x < 10 or y < 10 :
        return negative * x * y
    HalfLengthOfLongestNumber = max(len(str(x)), len(str(y))) // 2
    a, b, c, d = x // 10**HalfLengthOfLongestNumber, x % 10**HalfLengthOfLongestNumber, y // 10**HalfLengthOfLongestNumber, y % 10**HalfLengthOfLongestNumber
    ac, bd = karatsuba(a, c), karatsuba(b, d)
    return negative * (ac * (10**(2 * HalfLengthOfLongestNumber)) + (karatsuba(a + b, c + d) - ac - bd) * (10**HalfLengthOfLongestNumber) + bd)
