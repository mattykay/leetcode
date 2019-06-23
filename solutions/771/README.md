# 771. Jewels and Stones

Easy - https://leetcode.com/problems/jewels-and-stones/

## Problem

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

## Solution

Very basic. Simply iterate over each character in S (stones), if in J (valid jewels) increment result by one. o(n) solution which seems fine for this application, possibly could improve on memory by using another data type or calculated function instead of a result variable.

## Result

Runtime: 16 ms, faster than 92.74% of Python online submissions for Jewels and Stones.
Memory Usage: 11.7 MB, less than 54.26% of Python online submissions for Jewels and Stones.