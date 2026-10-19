class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        hash = defaultdict(list)
        for item in strs:
            count = [0] * 26
            for c in item:
                count[ord(c) - ord("a")] += 1
            hash[tuple(count)].append(item)
        return list(hash.values())
