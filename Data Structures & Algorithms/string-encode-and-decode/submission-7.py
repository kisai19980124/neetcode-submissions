class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty"
        for n in range(len(strs)):
            if "|" in strs[n] or "/" in strs[n]:
                strs[n] = strs[n].replace("/","//")
                strs[n] = strs[n].replace("|","/|")
        encoded_string = "|".join(strs)

        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split("|")
        n = 0
        if s == "empty":
            decoded_strs = []
            return decoded_strs
        while n < len(decoded_strs):
            count = decoded_strs[n].count("/")
            if count == 0:
                n=n+1
                continue
            elif count % 2 == 0:
                decoded_strs[n] = decoded_strs[n].replace("//","/")
                n=n+1
            else:
                decoded_strs[n] = decoded_strs[n]+"|"+decoded_strs[n+1]
                decoded_strs[n] = decoded_strs[n].replace("/|","|").replace("//","/")
                decoded_strs.pop(n+1)
        if len(decoded_strs) == 0:
            decoded_strs = []
        return decoded_strs