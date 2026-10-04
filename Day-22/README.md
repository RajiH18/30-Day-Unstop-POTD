Problem Statement
Meera runs the visitor flow desk at a large exhibition hall. Every guest passing through the main corridor scans a badge that records a collection number identifying the gallery they most recently visited, and the hall's system logs these numbers one after another for the entire day, in the exact order guests walked through. The collection numbers themselves are arbitrary identifiers assigned years ago and can be any large value, with no particular pattern to their size.

Later, while reviewing the day, Meera receives a list of specific stretches of the corridor log she is curious about, each stretch given as a starting position and an ending position within the day's recorded sequence. For every such stretch, she wants to know how strongly any single gallery dominated that particular stretch, meaning the largest number of times any one collection number repeated among the entries within that stretch. She is not interested in which gallery it was, only in how concentrated the busiest one was, since this figure helps her decide whether a stretch needs an extra staff member directing traffic.

Because the day's log can be very long and she may ask about many overlapping and non overlapping stretches at once, checking each stretch by scanning it from scratch every time is far too slow for her review meeting. She needs the answers computed for every requested stretch efficiently, honoring the exact order in which entries appear in the log, and handling collection numbers of any size without assuming they are small or sequential.

Input Format
The first line contains two integers n and q, the length of the day's log and the number of stretches asked about.
The second line contains n integers, the collection numbers in the order they were recorded.
Each of the next q lines contains two integers l and r (1-indexed, inclusive), describing one stretch.
Output Format
For each stretch, output one line containing a single integer, the largest repeat count of any collection number within that stretch.

Constraints
1 ≤ n, q ≤ 200000

1 ≤ collection number ≤ 1000000000

Sample Testcase 0
Testcase Input
8 3
5 5 5 5 6 6 7 7
1 2
1 8
5 8
Testcase Output
2
4
2
Explanation

Stretch [1,2] contains two entries of code 5, giving a peak of 2.

Stretch [1,8] contains four entries of code 5, which is the largest peak across the whole log.

Stretch [5,8] contains two entries each of codes 6 and 7, so the peak is 2.

Sample Testcase 1
Testcase Input
6 2
10 20 10 10 30 20
1 4
3 6
Testcase Output
3
2
Explanation

Stretch [1,4] contains entries 10, 20, 10, 10, so code 10 repeats 3 times.

No other code in that stretch repeats more than once.

Stretch [3,6] contains entries 10, 10, 30, 20, so code 10 repeats 2 times.

That is the highest repeat count in the second stretch.
