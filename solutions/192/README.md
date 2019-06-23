# 192. Word Frequency

Medium - https://leetcode.com/problems/word-frequency/

## Problem

Write a bash script to calculate the frequency of each word in a text file words.txt.

For simplicity sake, you may assume:

    words.txt contains only lowercase characters and space ' ' characters.
    Each word must consist of lowercase characters only.
    Words are separated by one or more whitespace characters.

## Solution

```
# Read from the file words.txt and output the word frequency list to stdout.
tr ' ' '\n' < words.txt | sort | sed '/^$/d' | egrep "(^[a-zA-Z]+)" | uniq -c | awk '{print $2 " " $1}' | sort -n -k2 -r
```
Translate file into words, sort them, delete empty lines, grep for those that start with letters, count unique values, output to required format before sorting by descending numeric frequency.

Probably a tad confusing at first glance, but use of Unix pipes here enable a one-liner result that is probably more efficient than using something like Python. Unsure what to improve on, as gets a good result.

## Result

Note: I feel as though the following result has to be a bug? 0ms?? (previous attempt showed 4ms, which is better than 88%)

Runtime: 0 ms, faster than 100.00% of Bash online submissions for Word Frequency.
Memory Usage: 3.3 MB, less than 86.55% of Bash online submissions for Word Frequency.