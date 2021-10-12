from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return self.search_min(nums)

    def search_min(self,nums):
        l = 0
        h = len(nums)-1
        m = 2468987
        while(l<=h):
            if (l==h):
                m = min(m,nums[h])
                l = h+1
                continue
            mid = int((l+h)/2)
            if nums[l] < nums[mid]:
                m = min(m,nums[l])
                l = mid + 1
                continue
            if nums[mid] < nums[h]:
                m = min(m,nums[mid])
                h = mid - 1
                continue
            if nums[h] < nums[mid]:
                m = min(m,nums[h])
                return m
            if nums[l] > nums[mid]:
                m = min(m,nums[mid])
                return m
        return m

obj = Solution()
print(obj.findMin([4,5,6,7,0,1,2]))
print(obj.findMin([5,1,2,3,4]))
print(obj.findMin([2,3,4,5,1]))
print(obj.findMin([2,3,1]))