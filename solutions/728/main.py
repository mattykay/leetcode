class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [
            value for value in range(left, right + 1)
            if self.divisibleBySelf(value)
        ]

    def divisibleBySelf(self, value: int) -> bool:
        for int_value in str(value):
            if int(int_value) == 0 or value % int(int_value) != 0:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.selfDividingNumbers(
        1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert s.selfDividingNumbers(47, 85) == [48, 55, 66, 77]
