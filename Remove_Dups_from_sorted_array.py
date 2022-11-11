class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        start=0
        temp=1
        prev=nums[0]
        k=1
        for i in nums:
            if i!=prev:
                k+=1
                prev=i
        i=1
        while i < k:
            while temp<n and start< k and nums[start]>=nums[temp] :
                temp+=1
            if nums[start]<nums[temp]:
                start+=1
                nums[start],nums[temp]=nums[temp],nums[start]
                i+=1
        return k
                
           
