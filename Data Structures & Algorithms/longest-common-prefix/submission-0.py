class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            prefix = strs[0]
            for word in strs[1:]:
                while not word.startswith(prefix):
                    prefix = prefix[:-1]
                    if prefix == "":
                        return ""
            return prefix