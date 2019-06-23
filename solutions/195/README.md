# 195. Tenth Line

Easy - https://leetcode.com/problems/tenth-line/

## Problem

Given a text file file.txt, print just the 10th line of the file.

Example:

Assume that file.txt has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10

Your script should output the tenth line, which is:

Line 10

## Solution

```
# Read from the file file.txt and output the tenth line to stdout.
lines=`wc -l file.txt | awk '{print $1}'`

if [[ $lines -ge 10 ]]
    then
    head -n 10 file.txt | tail -n 1
fi
```

A bit hacky, but effectively count lines using wc, then getting value from awk (since output contains file name). If this is greater than 10 obtain the 10 top values via head before outputting the last only using tail. Simply doing nothing if does not meet that length condition.


## Result

Runtime: 4 ms, faster than 87.78% of Bash online submissions for Tenth Line.
Memory Usage: 3.8 MB, less than 13.04% of Bash online submissions for Tenth Line.
