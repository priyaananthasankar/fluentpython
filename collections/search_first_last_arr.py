from typing import List
# Search first and last occurrance of a target in
# a sorted array in O(log n) time
# [2,4,8,8,8,9,10] = [2,4] is the first and last
# occurance of the target 8
# O(n) is easy solution but the challenge is to do this in O(log n)
class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        first = self.findBounds(nums, target, True)
        if first == -1:
            return[-1,-1]
        last = self.findBounds(nums, target,False)
        return[first,last]
        
        
    def findBounds(self,nums,target,isFirst):
        begin = 0
        end = len(nums)-1
        while(begin <= end):
            mid = int((begin + end)/2)
            if nums[mid] == target:
                # clearly nums[mid] isnt the first occurrance
                if isFirst:
                    if mid == begin or nums[mid-1] < target:
                        # we have found first occurance
                        return mid
                    
                    else:
                        end = mid-1
                else:
                    if mid == end or nums[mid+1] > target:
                        # we have found last occurance
                        return mid
                    
                    else:
                        begin = mid + 1
            if nums[mid] > target:
                 end = mid-1
            if nums[mid] < target: 
                 begin = mid + 1
        return -1

obj = Solution()
print(obj.searchRange([2,4,8,8,8,9,10],8))   
            