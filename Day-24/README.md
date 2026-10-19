Problem Statement
Nisha runs the end of day settlement desk at a small trading firm. Throughout the session her desk receives a stream of trade notices, each reporting that a certain ticker has just traded a batch of units. The same ticker can appear many times during the day, and each notice simply adds its unit count onto whatever total that ticker has accumulated so far during the current settlement window.

At certain points during the session, the desk head asks Nisha for the current leader: the ticker with the highest accumulated unit total across every notice received so far. If two tickers are tied for the highest total, the one with the numerically smaller ticker code is reported. As soon as Nisha reports a ticker as the leader, that ticker is considered settled for this window and its accumulated total resets to zero, so it can begin building up again from later trade notices without affecting the outcome of earlier settlements.

Ticker codes are plain identifying numbers assigned by the exchange and are not guaranteed to be small or sequential, since new tickers get listed and delisted constantly. Nisha needs a way to answer every leader request instantly, even though thousands of trade notices and leader requests can arrive back to back in a single session, and even though the leaderboard keeps shifting as totals rise and periodically drop back to zero. It is guaranteed that whenever the desk head asks for the leader, at least one ticker currently holds a strictly positive accumulated total, so a valid answer always exists. Nisha wants a clean log showing, for every leader request in order, which ticker settled and how many units it had accumulated at that moment.

Input Format
Line 1: a single integer n, the number of events.
Each of the next n lines is either:
BUY id units meaning ticker id traded units more units, or
PEAK meaning the desk head asks for the current leader.
Output Format
For every PEAK event, in the order they occur, print a line containing the settled ticker id followed by its accumulated unit total at settlement time.

Constraints
1 <= n <= 3 * 10^5

1 <= id <= 10^9

1 <= units <= 10^4

At least one PEAK event occurs only when some ticker currently has a strictly positive total.

Sample Testcase 0
Testcase Input
5
BUY 5 10
BUY 3 10
PEAK
BUY 3 5
PEAK
Testcase Output
3 10
5 10
Explanation

Tickers 5 and 3 are tied at 10 units each after the first two notices.

The tie is broken by the smaller ticker code, so 3 settles first and resets to zero.

A later notice brings ticker 3 back up to 5 units, but ticker 5 still holds 10 units.

The second PEAK reports ticker 5 with its untouched total of 10.

Sample Testcase 1
Testcase Input
6
BUY 101 50
BUY 202 30
BUY 101 20
PEAK
BUY 202 10
PEAK
Testcase Output
101 70
202 40
Explanation

After the first three notices, ticker 101 has 70 units and ticker 202 has 30 units.

The first PEAK reports 101 with 70, then resets 101 back to zero.

A further notice raises ticker 202 to 40 units while 101 stays at zero.

The second PEAK reports 202 with 40, since it is now the highest total.