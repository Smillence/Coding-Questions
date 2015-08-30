# There are two sorted arrays nums1 and nums2 of size m and n respectively. 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArray(self, nums):
        if not nums:
            return None
        n = len(nums)
        return (nums[n/2] + nums[n - n/2 - 1]) / 2.0
        
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        return self.findMedianSortedArraysHelper(nums1, nums2)
        
    def findMedianSortedArraysHelper(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        if n1 <= 2:
            if n2 <= 2:
                return self.findMedianSortedArray(sorted(nums1 + nums2))
            else:
                L = n2 - n2/2 - 2
                R = n2/2 + 2
                return self.findMedianSortedArray(sorted(nums1 + nums2[L:R]))
                
        m1 = self.findMedianSortedArray(nums1)
        m2 = self.findMedianSortedArray(nums2)
        if m1 == m2:
            return m1
            
        x = n1 - n1/2 - 1
        if m1 > m2:
            return self.findMedianSortedArrays(nums1[:-x], nums2[x:])
        else:
            return self.findMedianSortedArrays(nums1[x:], nums2[:-x])