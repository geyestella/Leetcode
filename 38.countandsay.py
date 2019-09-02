class Solution(object):
    def searchInsert(nums, target):
        if (target<nums[0]):
            return 0
        elif (target>nums[len(nums)-1]):
            return len(nums)
        else: 
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                if ((nums[i]< target) & (nums[i+1]> target)):
                    return i+1
                    
    def searchInsert1(nums, target):
        l , r = 0, len(nums)-1
        while l <= r:
            mid=int((l+r)/2)
            if nums[mid]== target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l             

    print(searchInsert1([1],1))