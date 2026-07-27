class Solution(object):
    def sortedSquares(self, nums):
       n=len(nums)
       left=0
       right=n-1
       result=[]
       while left<=right:
        if abs(nums[left])>abs(nums[right]):
             result.append(nums[left]**2)
             left=left+1
        else:
            result.append(nums[right]**2) 
            right=right-1
       result.reverse()
       return result         