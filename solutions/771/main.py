class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = 0
        for char in S:
            if char in J:
                result += 1
        return result

if __name__ == "__main__":
    s = Solution()
    assert s.numJewelsInStones("aA", "aAAbbbb") == 3
    assert s.numJewelsInStones("z", "ZZ") == 0