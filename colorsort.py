class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red=0
        white=0
        blue=0
        for i in nums:
            if i==0:
                red+=1
            if  i==0:
                 white+=1
            if i==0:
               blue+=1
        pos=0
        for j in range(red):
            nums[pos]=0
            pos+=1
        for j in range(white):
            nums[pos]=1
            pos+=1
        for j in range(blue):
            nums[pos]=2
            pos+=1
