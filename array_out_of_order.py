"""
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. 
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element 
appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: 
(2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair 
forms an inversion.
"""
def countAndMerge(nums):
    if len(nums) <= 1:
        return nums, 0
    mid = len(nums) // 2
    leftNums, leftCount = countAndMerge(nums[:mid])
    rightNums, rightCount = countAndMerge(nums[mid:])
    leftIdx, rightIdx = 0, 0
    count = leftCount + rightCount
    for i in range(len(nums)):
        if leftIdx == len(leftNums):
            nums[i] = rightNums[rightIdx]
            rightIdx += 1
        elif rightIdx == len(rightNums):
            nums[i] = leftNums[leftIdx]
            leftIdx += 1
        elif leftNums[leftIdx] <= rightNums[rightIdx]:
            nums[i] = leftNums[leftIdx]
            leftIdx += 1
        else:
            nums[i] = rightNums[rightIdx]
            rightIdx += 1
            count += len(leftNums) - leftIdx
    return nums, count


def countInversion(nums):
    _, inversions = countAndMerge(nums)
    return inversions

if __name__ == "__main__":
    print(countInversion(list(range(10))))
    print(countInversion(list(reversed(range(10)))))
    print(countInversion([1,2,3,4,6,5]))