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
        
           2. Bit Manipulation - XOR is what I can think about here.
        '''
       if not nums:
           return 0
       n = len(nums)
       sum_of_nums = 0
       sum_of_n = 0
       
       for i in xrange(n):
           sum_of_nums += 1
       sum_of_n = (n * (n+1))//2
       return sum_of_n - sum_of_nums
        
        
