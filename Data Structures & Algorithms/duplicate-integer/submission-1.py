class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        len_nums = len(nums)
        for i in range(len_nums-1):
            if nums[i] == nums[i+1]:
                return True
        return False
