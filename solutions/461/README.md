# 461. Hamming Distance

Easy - https://leetcode.com/problems/hamming-distance/

## Problem

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231. 

## Solution

Fairly simple. Perform exclusive-or (XOR) on input ints and counts the 1's in the binary conversion as these indicate differences and thus Hamming distance. 

(i.e. 1 = 1 in binary, 4 = 100 in binary, so 001 XOR 100 = 101) 

## Result

Runtime: 16 ms, faster than 88.09% of Python online submissions for Hamming Distance.
Memory Usage: 11.7 MB, less than 70.19% of Python online submissions for Hamming Distance.