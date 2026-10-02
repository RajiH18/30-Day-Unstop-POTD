Problem Statement
Diego reviews a season's worth of match performance entries for a multi team league, listed in strict chronological order. Each entry names the team involved and a performance rating earned that match. Because many teams play interleaved with one another throughout the season, a single team's entries are scattered among entries belonging to other teams.

For every entry, Diego wants to know how many entries pass, counting only from that entry onward in the full chronological list, before that same team records a strictly higher rating than the one in the current entry. Entries belonging to other teams in between do not count toward this waiting figure at all, since Diego only cares about a team's own momentum relative to itself. If a team never again beats its rating from a given entry for the remainder of the season, that entry simply has no answer.

Once every entry's waiting figure has been worked out, Diego wants a separate leaderboard highlighting the K entries across the entire season, regardless of team, that took the longest to be topped by their own team's next better performance. Entries with no answer at all are excluded from this leaderboard entirely, since an undefined wait cannot be meaningfully compared to a finite one. When two entries share the same waiting figure, the one that occurred earlier in the season is considered the more notable slow burn and should be listed first; if fewer than K entries have a finite waiting figure at all, the leaderboard simply lists however many qualify.

Teams are identified by numeric franchise codes rather than names, since some franchises have rebranded mid season, and only the numeric code is trusted for grouping entries together correctly.

Given the full chronological list of entries and the leaderboard size K, produce every entry's waiting figure in order, followed by the leaderboard of entry positions.

Input Format
Line 1 contains two integers n and K, the number of entries and the leaderboard size.
Each of the next n lines contains two integers t_i and r_i, the franchise code and performance rating of the i-th entry, in chronological order.
Output Format
Print two lines. The first line contains n integers, the waiting figure for each entry in order, using -1 for entries with no answer. The second line contains the 1-indexed positions of the leaderboard entries, ordered as described, space separated.

Constraints
1 <= n <= 2 * 10^5

1 <= K <= n

1 <= t_i <= 10^9

1 <= r_i <= 10^9

Time Limit: 2 seconds, Memory Limit: 256 MB

Sample Testcase 0
Testcase Input
8 3
3 10
9 8
3 5
3 12
9 9
3 7
9 15
3 20
Testcase Output
3 3 1 4 2 2 -1 -1
4 1 2
Explanation

Entry 1 (team 3, rating 10) is next beaten by entry 4 (rating 12), a wait of 3; entry 3 (rating 5) is beaten sooner by entry 4 as well, a wait of just 1.

Entry 2 (team 9, rating 8) is beaten by entry 5 (rating 9), a wait of 3, while entry 5 itself is beaten later by entry 7 (rating 15), a wait of 2.

Entries 7 and 8 are never topped again by their own teams for the rest of the season, so both are -1.

The three largest finite waits belong to entries 4, 1, and 2, in that order once ties are broken by earlier position.

Sample Testcase 1
Testcase Input
5 5
1 100
1 50
1 90
2 5
2 5
Testcase Output
-1 1 -1 -1 -1
2
Explanation

Entry 1 (rating 100) and entry 3 (rating 90) are never beaten again by team 1, so both are -1.

Entry 2 (rating 50) is beaten by entry 3 (rating 90), a wait of 1.

Entries 4 and 5 both belong to team 2 with equal ratings, and equal is not strictly higher, so neither beats the other, leaving both -1.

Only one entry has a finite wait at all, so the leaderboard of size 5 simply lists that single entry.
