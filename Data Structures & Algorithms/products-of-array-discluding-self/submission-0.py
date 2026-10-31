class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        if nums.count(0) > 1:
            return output
        elif nums.count(0) == 1:
            product = 1
            zero_i = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    product = product * nums[i]
                else:
                    zero_i = i
            for i in range(len(nums)):
                if i == zero_i:
                    output[i] = product
                else: 
                    output[i] = 0
        else:
            product = 1
            for i in range(len(nums)):
                product = product * nums[i]
            for i in range(len(nums)):
                output[i] = int( product / nums[i] )
        return output