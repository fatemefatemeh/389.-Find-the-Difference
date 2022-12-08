class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sums=0
        sumt=0
        for i in s:
            sums+=ord(i)
        for i in t:
            sumt+=ord(i)
        return chr(sumt-sums)