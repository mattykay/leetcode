from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        LENGTH = len(deck)
        SORTED_DECK = sorted(deck)
        INDEXES = deque([index for index in range(LENGTH)])
        VALUES = [None] * LENGTH

        for index in range(LENGTH):
            VALUES[INDEXES.popleft()] = SORTED_DECK[index]
            if INDEXES:
                INDEXES.append(INDEXES.popleft())
        return VALUES


if __name__ == "__main__":
    s = Solution()
    assert s.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]) == [2,13,3,11,5,17,7]
