Problem Statement
Dev tracks a daily momentum score for a stock he follows, one integer per trading day, and he believes a day's momentum is only meaningful in the context of how "normal" it looks compared to recent history. Before he logs each new day's score into his ledger, he wants to note how many earlier days in the ledger had a score close to today's specifically, within a fixed tolerance K in either direction, so a score of 8 with tolerance 2 is considered close to any earlier score between 6 and 10 inclusive.

The tolerance K is fixed for the whole ledger, chosen once at the start of the trading period based on how volatile Dev expects the stock to be. On the very first day there is no history yet, so that day always logs a closeness count of zero. From the second day onward, Dev looks back only at days already logged before the current one, never at the current day's own score or at any future day.

Momentum scores can repeat exactly, can be zero, and can be quite large, since they come from a compound formula Dev's spreadsheet computes elsewhere; he only feeds the final integers into this ledger. He wants the full list of daily closeness counts produced in one pass through the trading period, matching the order the days occurred in, so he can paste it directly next to his existing score column without any manual realignment.

Help Dev generate this list of closeness counts efficiently, since some of his tracked periods span hundreds of thousands of trading days.

Input Format
Line 1: two integers n and K.
Line 2: n integers — the momentum scores in day order.
Output Format
Print n lines. The i-th line contains the number of earlier days (days 1 to i−1) whose score lies within K of day i's score.

Constraints
1 ≤ n ≤ 2×10^5

0 ≤ score ≤ 10^9

0 ≤ K ≤ 10^9

Sample Testcase 0
Testcase Input
5 2
5 7 3 6 9
Testcase Output
0
1
1
2
1
Explanation

Day 1 (score 5) has no earlier days, so the count is 0.

Day 2 (score 7) looks for earlier scores in [5,9]; only 5 qualifies, count 1.

Day 4 (score 6) looks for earlier scores in [4,8]; scores 5 and 7 qualify, score 3 does not, count 2.

Day 5 (score 9) looks for earlier scores in [7,11]; only 7 qualifies among {5,7,3,6}, count 1.

Sample Testcase 1
Testcase Input
4 0
10 10 10 20
Testcase Output
0
1
2
0
Explanation

With tolerance 0, a score only counts earlier days with the exact same score.

Day 2 (score 10) matches the single earlier 10, count 1.

Day 3 (score 10) matches both earlier 10s, count 2.

Day 4 (score 20) has no earlier day scoring exactly 20, count 0.