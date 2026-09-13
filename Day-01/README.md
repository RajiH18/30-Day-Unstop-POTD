# Day 01 - Dev's Wristband Console

## Problem
Find the top K wristband IDs based on their net scan count.

## Approach
- Store the scan count of each ID using a dictionary.
- Increase the count for `+`.
- Decrease the count for `-`.
- Keep only IDs with a positive final count.
- Sort the results.
- Return the top K IDs.

## Concepts Learned
- Python dictionaries
- Dictionary `.get()`
- For loops
- If conditions
- Lists
- Sorting
- Lambda functions

## Result
- Platform: Unstop
- Difficulty: Medium
- Status: Solved
- Score: 120/120