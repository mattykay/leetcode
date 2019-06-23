# 950. Reveal Cards In Increasing Order

Medium - https://leetcode.com/problems/reveal-cards-in-increasing-order/

## Problem

In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

    Take the top card of the deck, reveal it, and take it out of the deck.
    If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
    If there are still unrevealed cards, go back to step 1.  Otherwise, stop.

Return an ordering of the deck that would reveal the cards in increasing order.

The first entry in the answer is considered to be the top of the deck.

## Solution

Double ended queue type solution using popping. Effectively pre-sort list and initialise deque of indexes. Pop left index, storing the related sorted list as value list, before popping next index to end of deque which results in a revolving solution that iterates over length of deck.

E.g.
Values, Index
[None, None, None, None, None, None, None] deque([0, 1, 2, 3, 4, 5, 6])
[2, None, None, None, None, None, None] deque([2, 3, 4, 5, 6, 1])
[2, None, 3, None, None, None, None] deque([4, 5, 6, 1, 3])
[2, None, 3, None, 5, None, None] deque([6, 1, 3, 5])
[2, None, 3, None, 5, None, 7] deque([3, 5, 1])
[2, None, 3, 11, 5, None, 7] deque([1, 5])
[2, 13, 3, 11, 5, None, 7] deque([5])
[2, 13, 3, 11, 5, 17, 7] deque([])

Time complexity = O(n log n) since sorted

## Result

Runtime: 48 ms, faster than 78.75% of Python3 online submissions for Reveal Cards In Increasing Order.
Memory Usage: 13.3 MB, less than 26.26% of Python3 online submissions for Reveal Cards In Increasing Order.
