from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        occurrences = defaultdict(int)
        # Sort by occurrences
        for value in arr:
            occurrences[value] += 1

        # If set of occurrences is less than occurrences, it means duplicate values and hence not unique
        if len(set(occurrences.values())) < len(occurrences.values()):
            return False

        return True


if __name__ == "__main__":
    s = Solution()
    assert s.uniqueOccurrences([1, 2, 2, 1, 1, 3])
    assert not s.uniqueOccurrences([1, 2])
    assert s.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
