# 380. Insert Delete GetRandom O(1)

Medium - https://leetcode.com/problems/insert-delete-getrandom-o1/

## Problem

Design a data structure that supports all following operations in average O(1) time.

    insert(val): Inserts an item val to the set if not already present.
    remove(val): Removes an item val from the set if present.
    getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

## Solution

First attempt I used set's which I mistook for having dictionary like lookups (I was wrong :p)

Second attempt which is the solution submitted, I converted the logic to use dictionaries with values tracking position/indexes. Actual values stored to list achieving the O(1) intended speed, as dictionary for O(1) lookup, but list required to return random value in this case without compiling dictionary keys.

Time complexity = O(1)

## Result

Runtime: 112 ms, faster than 94.77% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 18.1 MB, less than 12.50% of Python3 online submissions for Insert Delete GetRandom O(1).
