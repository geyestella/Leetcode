class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_idx = 0
        while curr_idx < len(nums) - 1:
            if(nums[curr_idx]==nums[curr_idx+1]):
                del nums[curr_idx+1]
                curr_idx -= 1 
            curr_idx += 1
        return len(nums)
    
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))