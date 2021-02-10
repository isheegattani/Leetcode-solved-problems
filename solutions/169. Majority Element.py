class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=nums.count(i)
                print(dic)
        keymax=max(dic,key=dic.get) 
        print(keymax)
        if(dic[keymax]>=(len(nums)//2)):
            return keymax
        else:
            return None
        
 
