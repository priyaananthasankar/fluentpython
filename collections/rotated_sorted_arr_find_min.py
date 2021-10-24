from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return self.split_search(nums,0,len(nums)-1)
    
    def split_search(self,nums,l,h) -> int:  
        min = 10000000  
        while(l<=h):
            mid = int((l+h)/2)
            if nums[l] < nums[mid]:
                if nums[l] < min:
                    min = nums[l]
                # search right
                l = mid + 1
            elif nums[mid] > nums[h]:
                if nums[h] < min:
                    min = nums[h]
                # search left
                h = mid-1
            else:
                if nums[mid] < min:
                    min = nums[mid]
                    break
        # while (l<=h):
        #     mid = int((l+h)/2)
        #     if nums[mid-1] > nums[mid]:
        #         return nums[mid]
        #     elif nums[mid+1] < nums[mid]:
        #         return nums[mid + 1]
        #     else:
        #         # normal cases
        #         if nums[mid-1] < nums[mid]:
        #             # search left
        #             h = mid-1
        #         else:
        #             # search righ
        #             b = mid + 1
        # return nums[h]
        return min

        

obj = Solution()
print(obj.findMin([4,5,6,7,0,1,2]))
# print(obj.findMin([11,13,15,17]))
# print(obj.findMin([1]))
# print(obj.findMin([5,1,2,3,4]))
# print(obj.findMin([2,3,4,5,1]))
# print(obj.findMin([3,4,5,6,1,2]))