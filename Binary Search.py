#Binary Search Algorithm Implementation

def searchInsert(nums, target):
        lower_bound = 0
        upper_bound = len(nums) - 1
        mid_point = upper_bound // 2

        for i in range(len(nums)):
            if target > nums[mid_point]:
                upper_bound = mid_point + 1
                return upper_bound
            elif target == nums[mid_point]:
                return mid_point
            else:
                lower_bound = mid_point -1
                return lower_bound
            
