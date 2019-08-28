def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        newnums=[]
        
        for i in range(0,len(nums)):
            if (nums[i]!=val):
                newnums.append(nums[i])
        return newnums

print(removeElement([0,1,2,2,3,0,4,2],2))