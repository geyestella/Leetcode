def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        curr_idx = 0
        while curr_idx < len(nums) :
            if(nums[curr_idx]==val):
                del nums[curr_idx]
                curr_idx -= 1 
            curr_idx += 1
        return nums

print(removeElement([0,1,2,2,3,0,4,2],2))