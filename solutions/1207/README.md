# 1207. Unique Number of Occurrences

Easy - https://leetcode.com/problems/unique-number-of-occurrences/

## Problem

Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

## Solution

Count occurrences and then compare length of occurrences against length of set of occurrences. If they differ it implies duplicate values, and hence not unique.

After reviewing other solutions after, it appears this could even be a one liner using a set comprehension!

Time complexity = o(n) linear since i traverse whole list to sort by occurrence

## Result

Runtime: 40 ms, faster than 100.00% of Python3 online submissions for Unique Number of Occurrences.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Unique Number of Occurrences.

