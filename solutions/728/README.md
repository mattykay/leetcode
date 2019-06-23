# 728. Self Dividing Numbers

Easy - https://leetcode.com/problems/self-dividing-numbers/

## Problem

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:

Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

## Solution

Calculate range of values, pass each value to a function that splits each character of value into an integer and determines whether the value is divisible by this split integer, collating each value that is true to a list and returning.

Some optimisations were made as first attempt was faster that 20% (which is a nice way of saying slower than 80%!).

Originally tried to use Python's lru_cache module, but suprisingly added some overhead (I think because there isn't that much to cache unlike my first assumption?)

Additionally had another list comprehension that did the int conversion instead of at if evaluation as it is in code now, this meant some time was wasted calculating int conversion of all values which was not necessary.

Possibly further reduction of brute force approach could be done as currently o(n) time.

## Result

Runtime: 60 ms, faster than 60.91% of Python3 online submissions for Self Dividing Numbers.
Memory Usage: 13.3 MB, less than 15.27% of Python3 online submissions for Self Dividing Numbers.