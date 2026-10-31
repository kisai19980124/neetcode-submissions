class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        suf = [0] * n
        out = [0] * n
        pre[0] = 1
        suf[n-1] = 1
        for i in range(1,n):
            pre[i] = pre[i-1] * nums[i-1]
            suf[n-1-i] = suf[n-i] * nums[n-i]
        for i in range(n):
            out[i] = pre[i] * suf[i]
        return out

