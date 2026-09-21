Problem Statement
Nisha works at a hydrology outpost that records the depth of a river every hour. Over the last n hours she has collected one depth reading per hour, and she now wants to publish short bulletins that help the flood-response team spot dangerous stretches of the river's behavior.

For every stretch of exactly W consecutive hours, Nisha wants to know two things at once: the highest depth reading recorded during that stretch, and how many genuinely different depth levels were observed during it. A stretch can have a modest peak but still be dangerous if the depth keeps swinging between many different levels, since that signals unstable upstream conditions; conversely a stretch with a single repeated depth is calm even if that depth is high.

She will slide her attention forward one hour at a time first hours 1 to W, then hours 2 to W+1, and so on until the last stretch ending at hour n and for each such stretch she writes down the peak reading and the count of distinct readings side by side, forming a bulletin sequence that the response team scans in order.

Help Nisha produce this bulletin sequence quickly, since the outpost's sensor network can report thousands of readings per session and she needs the bulletins published before the next reading arrives.

Input Format
Line 1: two integers n and W.
Line 2: n integers: the hourly depth readings.
Output Format
Print n − W + 1 lines. The i-th line contains two integers: the peak reading and the number of distinct readings in the i-th stretch.

Constraints
1 ≤ W ≤ n ≤ 2×10^5

0 ≤ reading ≤ 10^9

Sample Testcase 0
Testcase Input
5 2
7 7 7 7 7
Testcase Output
7 1
7 1
7 1
7 1
Explanation

Every stretch consists of two identical readings of 7.

The peak is always 7 since no other value appears.

Only one distinct value (7) ever appears in any stretch.

All four stretches therefore report the same bulletin.

Sample Testcase 1
Testcase Input
6 3
4 2 2 6 1 6
Testcase Output
4 2
6 2
6 3
6 2
Explanation

Stretch [4,2,2] has peak 4 and readings {4,2} → 2 distinct values.

Stretch [2,2,6] has peak 6 and readings {2,6} → 2 distinct values.

Stretch [2,6,1] has peak 6 and readings {2,6,1} → 3 distinct values.

Stretch [6,1,6] has peak 6 and readings {6,1} → 2 distinct values.s