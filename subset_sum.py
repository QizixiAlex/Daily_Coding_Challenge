"""
This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. 
If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""
def hasSubset(nums, k):
    dp = [[False for _ in range(k+1)] for _ in range(len(nums)+1)]
    for i in range(len(nums)+1):
        dp[i][0] = True
    for i in range(1, len(nums)+1):
        for j in range(1,k+1):
            if j < nums[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    return dp

def findSubset(nums, k):
    # construct one solution
    dp = hasSubset(nums, k)
    if not dp[-1][-1]:
        return None
    result = []
    i, j = len(nums), k
    while j != 0:
        if dp[i-1][j]:
            i -= 1
        else:
            result.append(nums[i-1])
            i, j = i-1, j-nums[i-1]
    return result

if __name__ == '__main__':
    print(findSubset([12, 1, 61, 5, 9, 2], 24))
