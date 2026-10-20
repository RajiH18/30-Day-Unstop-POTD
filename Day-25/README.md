Problem Statement
Meera leads a dig covering n numbered excavation zones scattered across a hillside, and each zone has already been classified with a single artifact category code based on early surface finds. Between many pairs of zones, the survey team has identified candidate tunnels that could physically connect them, and each candidate tunnel carries a digging cost reflecting how much rock must be cleared.

To keep the season's budget under control, Meera's crew digs candidate tunnels strictly in order of increasing cost, and they only ever dig a tunnel if the two zones it would join are not already reachable from one another through tunnels dug earlier; any tunnel that would simply reconnect zones already linked is skipped entirely to save effort. By the end of the season, this leaves the zones grouped into clusters, where every zone inside a cluster can be reached from every other zone in that same cluster using only the tunnels that were actually dug, while zones in different clusters remain unreachable from each other.

Once digging wraps up, Meera wants a summary of the season. She needs the total digging cost spent across every tunnel that was actually dug, along with a closer look at whichever cluster ended up containing the most zones, since that cluster represents the richest connected excavation site. Ties for the largest cluster are broken in favor of whichever cluster contains the zone with the smallest numbering. Within that single largest cluster, Meera also wants to know which artifact category appears most often among its zones, since that tells her team what to expect as they dig deeper there, with ties among categories broken by the smaller category code. This single seasonal report will guide next year's funding request.

Input Format
Line 1: two integers n and m, the number of zones and the number of candidate tunnels.
Line 2: n integers, the artifact category code of zones 1 through n.
Each of the next m lines contains three integers u, v, and cost, describing a candidate tunnel between zone u and zone v with the given digging cost.
Output Format
Print a single line containing four integers: the total digging cost spent, the size of the largest resulting cluster, the most frequent artifact category code within that cluster, and how many zones in that cluster carry it.

Constraints
1 <= n <= 2 * 10^5

0 <= m <= 4 * 10^5

1 <= u, v <= n, u != v

1 <= cost <= 10^9

1 <= category code <= 10^9

Sample Testcase 0
Testcase Input
5 4
10 10 20 20 10
1 2 5
2 3 8
3 4 3
4 5 7
Testcase Output
23 5 10 3
Explanation

Tunnels are dug in cost order 3, 5, 7, 8, merging all five zones into one cluster.

The total digging cost is 3 + 5 + 7 + 8 = 23.

The single cluster holds all 5 zones, so its size is 5.

Among categories 10, 10, 20, 20, 10, category 10 appears 3 times, more than category 20.

Sample Testcase 1
Testcase Input
6 3
5 5 5 7 7 7
1 2 4
2 3 6
4 5 2
Testcase Output
12 3 5 3
Explanation

Tunnels are dug in cost order 2, 4, 6, forming clusters {4,5}, {1,2,3}, and isolated zone {6}.

The total digging cost is 2 + 4 + 6 = 12.

The largest cluster is {1,2,3} with size 3, beating the size-2 and size-1 clusters.

All three zones in that cluster carry category 5, so it wins with a count of 3.