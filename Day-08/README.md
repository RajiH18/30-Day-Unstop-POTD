Problem Statement
Dr. Elena Voss directs recovery efforts at the Kharantep Ruins, a lattice of underground chambers linked by tunnels that collapsed centuries ago and are now being cleared out one tunnel at a time. Each chamber was originally sealed with at most one relic, valued according to the site's independent appraisal; some chambers, disturbed long ago by looters, hold no relic at all. As tunnels are cleared during the dig, previously isolated chambers become mutually reachable, and Elena's crew can walk freely between any two chambers that now lie in the same cleared out pocket of the ruins.

Whenever the crew reaches a chamber, they can request that the single most valuable unclaimed relic reachable from it be brought to the surface immediately, without waiting for the rest of that pocket to be fully excavated. Once a relic is claimed it is gone for good, no matter how many further tunnels are later cleared into that pocket. If two unclaimed relics reachable from the requested chamber are tied for the highest value, the crew always prefers the one sitting in the lower numbered chamber, since its excavation paperwork was filed first and its removal permit is already signed.

Tunnels are cleared strictly in the order recorded in the site log, and a retrieval request can arrive at any point in that log, interleaved freely with tunnel clearances. A chamber may appear in several tunnel clearances over the course of the dig as more of the ruins opens up, and the same chamber may also be the target of several retrieval requests at different times. It is guaranteed that a tunnel is only recorded once it has actually been cleared, and a chamber's own relic, if it has one, always counts as reachable from itself even before any tunnel touching that chamber has been cleared.

The funding committee has asked Elena for a live account of every retrieval, since each recovered relic needs to be logged with its chamber of origin before it leaves the site. Given the full site log, help Elena report, for every retrieval request, the value of the relic that surfaces and which chamber it came from, or state plainly that nothing remains to retrieve from that chamber's pocket.

Input Format
Line 1: two integers n and m, the number of chambers and the number of log entries.
Line 2: n integers, the initial relic value of chambers 1 through n (0 means empty).
Each of the next m lines is one of:
LINK u v
CLAIM x
Output Format
For every CLAIM entry, print either two values "chamber value" for the relic that surfaced, or the single word "EMPTY".

Constraints
1 <= n, m <= 2*10^5

0 <= relic value <= 10^9

1 <= u, v, x <= n

Sample Testcase 0
Testcase Input
5 6
10 0 30 5 30
LINK 1 2
CLAIM 1
LINK 3 4
LINK 1 3
CLAIM 5
CLAIM 1
Testcase Output
1 10
5 30
3 30
Explanation

Chambers 1 and 2 link first; chamber 1's own relic (10) is the only one reachable, so it is claimed.

Chambers 3 and 4 then link, and chamber 1's pocket links into that pocket next.

Chamber 5 is untouched by any tunnel, so its own relic (30) is claimed directly.

Chamber 1's pocket now contains chambers 1 through 4, whose only remaining relic is chamber 3's (30), so that surfaces.

Sample Testcase 1
Testcase Input
4 5
0 40 40 0
LINK 2 3
CLAIM 2
LINK 1 4
CLAIM 1
CLAIM 3
Testcase Output
2 40
EMPTY
3 40
Explanation

Chambers 2 and 3 hold tied relics of value 40; once linked, the lower numbered chamber's relic (chamber 2) is preferred and claimed first.

Chambers 1 and 4 link next, but neither ever held a relic, so their pocket reports EMPTY.

Chamber 3's pocket still holds its own relic since only chamber 2's was claimed, so it surfaces on the final request.