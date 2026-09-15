Problem Statement
Kabir maintains the electrified signal network for a heritage narrow-gauge railway, where every junction beyond the main depot connects back to exactly one earlier junction through a single stretch of track, so the whole layout forms one branching structure with the depot as its root. Every stretch of track is either electrified or shut off for maintenance at any given moment, and this status only ever changes one stretch at a time an engineer walks out, flips a breaker at some junction, and the single stretch feeding that junction from its parent junction toggles state.

Meanwhile, the control room keeps getting calls from drivers asking whether a specific journey between two junctions is fully usable, and Kabir answers by counting how many electrified stretches lie along the unique path between those two junctions a driver only cares about the count, since a single dead stretch anywhere still means someone has to walk that gap with a lantern.

At the start of the shift every stretch of track is electrified. Over the course of the shift, engineers flip breakers and drivers call in questions in some interleaved order, and Kabir has to answer each question the instant it comes in, using whatever the breaker states happen to be at that moment not before, not after.

Figure:

  (1) Depot
               /          \
            (2)            (3)
           /    \             \
        (4)      (5)          (6)
Toggling the stretch feeding junction 2 affects only that one stretch (depot–2), not the stretches deeper inside junction 2's branch.

Input Format:

The first line contains an integer n: the number of junctions (the depot is junction 1).
Each of the next n-1 lines contains two integers u and v:a track stretch directly connecting junctions u and v in the initial layout. The next line contains an integer q:the number of events.
Each of the next q lines is one of:
    1 v: toggle the electrified state of the stretch feeding junction v from its parent.
    2 u v: report how many electrified stretches lie on the path between junctions u and v.

Output Format:

For every event of type 2, print the requested count on its own line, in the order the events occur.

Constraints:

2 <= n <= 100000

1 <= q <= 200000

All stretches are electrified at the start of the shift.

Recomputing a path's stretch count by walking it node-by-node for every query can cost O(n) per query, which is far too slow across up to 200000 events; both toggling and answering must be handled without ever walking the full path.

Sample Testcase 0:

Testcase Input
3
1 2
1 3
3
2 2 3
1 2
2 2 3

Testcase Output:

2
1

Explanation:

Both stretches start electrified, so the path between junctions 2 and 3 (through the depot) crosses both of them, giving 2.

After toggling junction 2's feeding stretch off, the same path only has the depot–3 stretch still electrified, giving 1.

Sample Testcase 1:

Testcase Input
6
1 2
1 3
2 4
2 5
3 6
5
2 4 6
1 2
2 4 6
1 4
2 4 5

Testcase Output:

4
3
1

Explanation:

Initially every stretch is electrified, so the path from 4 to 6 (through 2, 1, and 3) crosses four electrified stretches, giving 4.

Toggling junction 2's feeding stretch shuts off the depot–2 connection, so the same path from 4 to 6 now crosses only three electrified stretches: (2,4), (1,3), (3,6).

Toggling junction 4's feeding stretch next shuts off (2,4) as well, so the final query along the much shorter path from 4 to 5 (through junction 2) finds only the (2,5) stretch still electrified, giving 1.
