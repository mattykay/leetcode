from random import randrange


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._positions = dict()
        self._values = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self._positions:
            return False
        else:
            # Save length of values, which represents index
            self._positions[val] = len(self._values)
            self._values.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self._positions:
            return False

        position = self._positions[val]
        del self._positions[val]

        if position == len(self._values) - 1:
            self._values.pop()
        else:
            last = self._values.pop()
            self._values[position] = last
            self._positions[last] = position

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self._values[randrange(len(self._values))]


if __name__ == "__main__":
    obj = RandomizedSet()
    assert obj.insert(1)
    assert not obj.remove(2)
    assert obj.insert(2)
    assert (obj.getRandom() == 1 or obj.getRandom() == 2)
    assert obj.remove(1)
    assert not obj.insert(2)
    assert obj.getRandom() == 2

    obj = RandomizedSet()
    assert obj.insert(3)
    assert obj.remove(3)
    assert not obj.remove(0)
    assert obj.insert(3)
    assert obj.getRandom() == 3
    assert not obj.remove(0)
