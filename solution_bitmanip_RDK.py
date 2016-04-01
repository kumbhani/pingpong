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
        
        We will try to do this using bit manipulation.
        
        First insight, the first and last numbers shouldn't be missing.
        if 0 is missing, then return "0"
        if nothing seems missing, return the last value + 1.
        '''
        
        if not nums:
          return 0
        n = len(nums)
        
        TrueCumXor = 0
        TestCumXor = 0
        
        for ii in xrange(0,len(nums)+1):
            TrueCumXor ^= ii
            if ii<len(nums):
                TestCumXor ^= nums[ii]
        return TrueCumXor^TestCumXor
            
