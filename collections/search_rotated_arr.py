from typing import List

# Searches a rotated array (that was sorted earlier)
# in O(log n) time by trying to guess at what pivot point
# the array is rotated

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.split_search(nums,0,len(nums)-1,target)
    
    def split_search(self,nums,l,h,t) -> int:
        if l>h:
            return -1
        mid = int((l+h)/2)
        
        # if t is found in mid return t
        if nums[mid] == t:
            return mid
        # if t < mid element, inspect left side more
        if nums[l] <= nums[mid]:
            # if t is between 0 and mid then search over left
            if t <= nums[mid] and t >= nums[l]:
                return self.split_search(nums,l,mid-1,t)
            # else search at right
            return self.split_search(nums,mid+1,h,t)
        
        # if t is beyond mid, narrow down to right side
        if t >= nums[mid] and t <= nums[h]:
                return self.split_search(nums,mid+1,h,t)
        # if lesser than mid then shift to left
        return self.split_search(nums,l,mid-1,t)

obj = Solution()
print(obj.search([4,5,6,7,0,1,2],1))
print(obj.search([4,5,6,7,0,1,2],3))
print(obj.search([4,5,6,7,0,1,2],4))
print(obj.search([4,5,6,7,0,1,2],7))