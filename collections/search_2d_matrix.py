from typing import List
# Search for element in a 2d matrix where
# each row is sorted in O(log n) time
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        for i in range(r):
            if self.searchRow(matrix[i],target):
                return True
        return False
      
    def searchRow(self,row_arr,target) -> bool:
        l = len(row_arr)-1
        
        if target == row_arr[0] or target == row_arr[l]:
           return True
        if target > row_arr[l]:
            return False
        if target > row_arr[0] and target < row_arr[l]:
            return self.binary_search(row_arr,target)
        
        
    def binary_search(self,row_arr,target):
        begin = 0
        end = len(row_arr)-1
        
        while(begin <= end):
            mid = int((begin+end)/2)
            if target == row_arr[mid]:
                return True
            elif target < row_arr[mid]:
                end = mid -1
            else:
                begin = mid + 1
        return False

obj = Solution()
print(obj.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
print(obj.searchMatrix([[1]],1))
print(obj.searchMatrix([[1],[3]],3))
print(obj.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))