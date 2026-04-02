from typing import List

class Solution:

    # Works for ascii input
    # O(n)
    def encodeDelim(self, strs: List[str]) -> str:
        if not strs:
            return ""

        return "•".join(strs)

    def decodeDelim(self, s: str) -> List[str]:
        if not s:
            return []

        return s.split("•")

    # Optimal neetcode.io solution
    # Time: O(m)
    # Space: O(m+n)
    def encodeOptimal(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decodeOptimal(self, s: str) -> List[str]:
        if not s:
            return []
            
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res
