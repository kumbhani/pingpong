'''
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

    For example,
    Given nums = [0, 1, 3] return 2.
    
    Note:
    Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''
class Solution(object):
    def missingNumber(self, nums):
        '''
        :type nums: List[int]
        :rtyp: int

        There are two approaches as hinted by the tags on leetcode.
           1. Math - Missing number would be the difference between
           the sum of n number minus sum of elements in in nums array
        
           2. Bit Manipulation - Using XOR, we set x1 as an accumulator like you mentioned for the elements in nums
           then x2 is set to 1 and then ran all the way to n. The remaining bits in x1 and x2 when XORed gives the 
           missing number
        '''
        if not nums:
            return 0
        x1 = nums[0]
        x2 = 1
        n = len(nums)
        for i in xrange(1, n):
            x1 ^= nums[i]
        for i in xrange(2, n+1):
            x2 ^= i
        return (x1 ^ x2)  
