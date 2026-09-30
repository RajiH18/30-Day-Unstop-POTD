Problem Statement

Anwar coordinates a wildlife conservation program that connects nature reserves with safe animal corridors. Each candidate corridor links two specific reserves and carries a fixed disturbance score, measuring how much a corridor interferes with nearby human activity such as roads and farmland. Lower scores mean quieter, safer corridors.



For a proposed journey between any two reserves, an animal does not travel along a single corridor but along a whole sequence of corridors, reserve to reserve, until it reaches its destination. The overall discomfort of such a journey is dictated entirely by its single worst corridor, since one heavily disturbed segment ruins the safety of the entire trip no matter how quiet the rest of the route was. Anwar therefore wants, for a given pair of reserves, the smallest possible value that the worst corridor along any connecting route could be, when the route is chosen as wisely as possible among every way of reaching the destination using the available corridors.



He has narrowed down a fixed list of candidate corridors that could realistically be built, each with its estimated disturbance score, and he has a batch of reserve pairs coming from different research teams asking exactly this question. Some reserves might not be reachable from each other at all using the candidate corridors, in which case there is no meaningful answer for that pair.



Given the list of reserves, the list of candidate corridors with their disturbance scores, and the batch of reserve pair questions, Anwar needs the smallest achievable worst-corridor value for each pair, or a clear signal that the pair cannot be connected at all.



Figure:

reserves:   1 --- 2 --- 3
                        |
                        4 --- 5 --- 6

corridor disturbance scores attached to each segment above
the safest route between 1 and 6 still has to cross whichever
single segment is unavoidable and most disturbed on that path

Input Format

Line 1 contains two integers n and m, the number of reserves and the number of candidate corridors.

Each of the next m lines contains three integers u_i, v_i, w_i, describing a candidate corridor between reserves u_i and v_i with disturbance score w_i.

The next line contains a single integer q, the number of reserve pair questions.

Each of the next q lines contains two integers a_i, b_i, the two reserves in that question.

Output Format

Print q lines. The i-th line contains the smallest achievable worst-corridor value for the i-th pair, or -1 if the two reserves cannot be connected using the candidate corridors.

Constraints

1 <= n <= 2 * 10^5

1 <= m <= 3 * 10^5

1 <= q <= 2 * 10^5

1 <= w_i <= 10^9

1 <= u_i, v_i <= n, u_i != v_i

1 <= a_i, b_i <= n

Time Limit: 2 seconds, Memory Limit: 256 MB

Sample Testcase 0

Testcase Input

5 3 1 2 4 1 3 7 3 4 2 2 2 4 2 5

Testcase Output

7 -1

Explanation

All three candidate corridors are needed to keep reserves 1, 2, 3, 4 reachable, since removing any one would split that group.

Reserve 2 to reserve 4 must pass through both the score 4 segment and the score 7 segment, so its worst unavoidable segment is 7.

Reserve 5 has no candidate corridor touching it at all, so it cannot be reached from reserve 2, giving -1.

Sample Testcase 1

Testcase Input

6 6 1 2 5 2 3 3 1 3 8 3 4 6 4 5 2 5 6 9 2 1 6 1 4

Testcase Output

9 6

Explanation

Building the cheapest connecting set of corridors first favors the smallest scores, ending up needing corridors of scores 2, 3, 5, 6, 9 to keep all six reserves reachable.

Reserve 1 to reserve 6 has only one sensible route once the cheap connecting set is fixed, passing through scores 5, 3, 6, 2, 9, so its worst unavoidable segment is 9.

Reserve 1 to reserve 4 follows the same connecting set but stops earlier, passing through scores 5, 3, 6, so its worst unavoidable segment is 6.

The corridor scored 8 between reserves 1 and 3 is never actually needed once cheaper corridors already keep everything reachable.