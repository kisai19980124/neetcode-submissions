class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)
        for num in nums:
            hash[num] += 1
        res= sorted(hash.items(), key = lambda x:x[1], reverse = True)
        result = [item[0] for item in res][0:k]
        return result