class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        for i in nums: 
            if nums[j]!=i:
                j=j+1
                nums[j]=i
        return j+1
        
                
            
