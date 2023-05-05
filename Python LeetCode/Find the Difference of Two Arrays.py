from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        check :set = set(nums1).intersection(set(nums2))
        return [[i for i in nums1 if i not in check], [i for i in nums2 if i not in check]]