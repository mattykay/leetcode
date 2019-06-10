# 193. Valid Phone Numbers

Easy - https://leetcode.com/problems/valid-phone-numbers/

## Problem

Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

## Solution

```
# Read from the file file.txt and output all valid phone numbers to stdout.
egrep "(^\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}$)|(^[0-9]{3}-[0-9]{3}-[0-9]{4}$)" file.txt
```

Fairly straight forward Regex solution - perhaps another utility might be more efficient however grep is my preferred bash CLI utility for text searching/regex.

## Result

Runtime: 8 ms, faster than 74.67% of Bash online submissions for Valid Phone Numbers.

Memory Usage: 3.1 MB, less than 34.23% of Bash online submissions for Valid Phone Numbers.