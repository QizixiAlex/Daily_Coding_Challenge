"""
Given a string, find the palindrome that can be made by inserting the fewest number of characters
as possible anywhere in the word. If there is more than one palindrome of minimum length that can
be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters 
to it (which is the smallest amount to make a palindrome). There are seven other palindromes that 
can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""

# solution https://www.geeksforgeeks.org/minimum-characters-added-front-make-string-palindrome/

def computeLPS(s):
    length = 0
    lps = [0 for _ in range(len(s))]
    i = 1
    while i < len(s):
        if s[i] == s[length]:
            # length is the current longest prefix & suffix length
            length += 1
            # lps[i] stores the longest prefix which is also a suffix of substring s[0..i]
            # hence lps[0] is always 0
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def findMinPalindrome(s):
    """
    example 1:
    ABC -> ABCCBA
    lps = computeLPS(ABCCBA)
    lps[-1] = 0
    return len(ABC) - 0 = 3
    example 2:
    AAB -> AABBAA
    lps[-1] = 1
    return 3-1 = 2
    BAAAB
    """
    revS = s[::-1]
    concatS = s + '$' + revS
    appendLen = len(s) - computeLPS(concatS)[-1]
    return revS[:appendLen] + s

if __name__ == '__main__':
    testCases = [
        'AAA',
        'AAB',
        'ABC'
    ]
    for case in testCases:
        print(findMinPalindrome(case))
