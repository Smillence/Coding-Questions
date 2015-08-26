'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

class Solution:
	  # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    # Note: the two numbers can be the same [0,1,2,0] 0
    # refer: http://www.cnblogs.com/zuoyuan/p/3698966.html
    # the key here is we don't need to add all nums to the dict before we stop; 
    # in this way, duplicate key is handle gracefully
    def twoSum(self, nums, target):
        dic = {}
        for i in xrange(len(nums)):
            key = nums[i]
            if target - key in dic:
                return [dic[target - key]+1, i+1]
            dic[key] = i
