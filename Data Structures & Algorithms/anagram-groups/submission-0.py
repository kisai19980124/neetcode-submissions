class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        hash = {}
        output = []
        i = 0
        for item in strs:
            sorted_item = "".join(sorted(item))
            if sorted_item in hash:
                output[hash[sorted_item]].append(item)
            else:
                hash[sorted_item] = i
                output.append([item])
                i = i + 1
        return output
