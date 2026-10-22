class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            s = s.replace("/","//").replace("|","/|")
            res.append(s+"|")
        encoded_string = "|".join(strs)

        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        current = []
        i = 0
        while i < len(s):
            if s[i] == "/":
                i +=1 #skip this "/"
                current.append(s[i]) #append the next character 
            elif s[i] == "|":
                res.append("".join(current))#current but list to string
                current = []
            else:
                current.append(s[i])
            i += 1
        return res