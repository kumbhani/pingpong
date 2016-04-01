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

      crap.. This isn't working because it assumes an ordered list of numbers. one of the test cases is [1,0] which returns 2.
      '''

      # Error checking the inputs
      if not nums:
        return 0

      # first value should be zero  -- Update, this isn't true, unless list is sorted..
      #if nums[0] != 0:
      #  return 0

      # Check if last value is missing
      if (len(nums)-1) != nums[-1]:
        return len(nums)

      # Check if intermediate vaule is missing, else return len(nums)
      for i in xrange(0,len(nums)):
        if nums[i]^i != 0:
          return i
      return len(nums)

