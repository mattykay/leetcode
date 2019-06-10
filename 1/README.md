# 1. Two Sum

Easy - https://leetcode.com/problems/two-sum/

## Problem

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Solution

Firstly group all int values and their index positions in a list (using a defaultdict to initialize list). Next iterate over input numbers, using each value calculate the complement (i.e. `target - number = complement`). Check if complement exists in dict, if so returning the lists for the value and complement (as it states only one solution) or if complement=number return its list. o(n) solution.

In a real world application, would need more error checking as it works based on assumptions stated. Runtime results good, but may need to review data structure or iterative process used if memory of concern.

## Result

Runtime: 28 ms, faster than 90.69% of Python online submissions for Two Sum.
Memory Usage: 15.3 MB, less than 5.04% of Python online submissions for Two Sum.