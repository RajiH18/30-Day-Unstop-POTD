Problem Statement
Naledi Dlamini monitors a transmission corridor for a regional grid operator, watching a line of turbines numbered 1 through n along its length. Every hour, each turbine records a single output reading, and safety regulations require any stretch of the corridor to be rated for the single highest reading any of its turbines reached during the period it was under evaluation. Naledi's engineering team runs periodic exposure reviews to decide how heavily different stretches of the corridor have been stressed historically.

Occasionally the team wonders about corridors that could have gone into service at different times. For a review covering hours l through r, the engineers imagine every hypothetical commissioning hour i between l and r inclusive, and ask what peak output rating the corridor would have needed if it had been switched on at hour i and monitored continuously through hour r. Summing these hypothetical peak ratings across every possible commissioning hour in the window gives the corridor's total exposure score for that review, since it reflects how much cumulative stress every plausible startup choice would have implied, and this score is what regulators actually use when approving future capacity upgrades along that stretch.

Because a single review window can involve a great many hypothetical commissioning hours once the corridor has been running for a while, and because Naledi's team submits many such review windows throughout a shift, checking every hypothetical start by hand quickly becomes impossible. Readings can vary wildly from hour to hour, sometimes climbing for a long stretch and sometimes staying essentially flat, and the exposure score has to reflect exactly what regulations define even when many hours share the same recorded output.

Review windows can arrive in any order and can end at any hour, not necessarily the most recent one processed so far, and a later review can revisit an hour that an earlier review already covered. Since the resulting exposure score can grow very large once the corridor has been active for a long time, Naledi reports every score modulo 1,000,000,007.

Given the full hourly reading log for the corridor and the day's list of review windows, help Naledi produce the exposure score for each one, in the order the reviews were submitted.

Figure:

Hour:      1    2    3    4
Reading:   3    1    4    2

After hour 3, hypothetical peaks for start=1,2,3 all equal 4.
Input Format
Line 1: an integer n, the number of hours recorded.
Line 2: n integers, the hourly readings a_1 through a_n.
Line 3: an integer Q, the number of review windows.
Each of the next Q lines: two integers l and r, a review window.
Output Format
For each review window, in input order, print its exposure score modulo 1,000,000,007 on its own line.

Constraints
1 <= n, Q <= 2*10^5

1 <= a_i <= 10^9

1 <= l <= r <= n

Sample Testcase 0
Testcase Input
4
3 1 4 2
2
2 4
1 4
Testcase Output
10
14
Explanation

Readings are 3, 1, 4, 2 for hours 1 through 4.

Once hour 3's reading of 4 arrives, the hypothetical peaks for starting at hour 1, 2, or 3 all rise to 4, while starting at hour 4 later gives 2.

For the window (2,4), the hypothetical peaks for starts 2, 3, 4 are 4, 4, 2, summing to 10.

For the window (1,4), adding start 1's peak of 4 gives a total of 14.

Sample Testcase 1
Testcase Input
5
2 2 2 2 2
2
1 5
3 5
Testcase Output
10
6
Explanation

All five hourly readings equal 2, so every hypothetical commissioning hour yields the same peak of 2 through hour 5.

All five hours are counted separately, even though they have the same peak value.

Summing 2 across the five hours in window (1,5) gives 10.

Summing 2 across the three hours in window (3,5) gives 6.