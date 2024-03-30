#LeetCode Problem 1 (Two Sum)

def twoSum(nums,target):
        for i in range(len(nums)):
            for p in range(i+1, len(nums)): 
             if i!=p and nums[i] + nums[p] == target:
                 return [i,p]

