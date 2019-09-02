class Solution(object):
    

    def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==1):
            return nums[0]
        i,j,MaxSum=0,len(nums)-1,-100000
        while i<j:
            SubSum = 0
            for k in range(i,j+1):
                SubSum += nums[k]
            MaxSum=max(MaxSum,SubSum)
            if (nums[i] < nums[j]):
                i+=1
            else:
                j-=1
        return MaxSum                

                        
    
                        
    print(maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]))