Problem Statement
Kabir runs a custom fabrication bay where each finished item occupies exactly one completion slot out of an enormous range of possible slots, since the bay has been operating for a very long time and slot numbers simply keep counting upward. He has just received a batch of pending custom orders for the day. Each order carries a profit value earned if completed, and a deadline slot, meaning the order must occupy some completion slot no later than that number, though it may be finished earlier if a slot is free. Every slot can host at most one order, and Kabir does not have to accept every order in the batch.

Kabir wants to choose which orders to accept and how to place each accepted order into some slot at or before its own deadline, so that the combined profit of everything accepted is as large as possible. Because the deadlines can be astronomically large numbers while the batch itself only ever contains a modest number of orders, Kabir knows intuitively that he will never actually need to reach far into those huge slot numbers, but he still wants a dependable procedure rather than guesswork before committing the bay's schedule for the day.

Before locking in the day's plan, he wants to know two things: the total profit the best possible arrangement would earn, and how many orders out of the batch end up accepted in that arrangement. He is not interested in the exact slot assignments themselves, only in these two summary figures, since the actual placement is handled separately by the bay's dispatch software once the accepted set is known.

Help Kabir compute this summary quickly even when the batch contains a large number of orders.

Input Format
The first line contains a single integer n, the number of pending orders.
Each of the next n lines contains two integers p and d, the profit and the deadline slot of one order.
Output Format
Output a single line containing two integers separated by a space: the maximum achievable total profit, followed by the number of orders accepted in that arrangement.

Constraints
1 ≤ n ≤ 200000

1 ≤ p ≤ 1000000000

1 ≤ d ≤ 1000000000

Sample Testcase 0
Testcase Input
4
100 1000000000
80 2
60 2
40 1
Testcase Output
240 3
Explanation

Since only 4 orders exist, no deadline beyond slot 4 is ever useful, so the huge deadline of order 1 behaves like slot 4.

Processing by profit from highest to lowest: order 1 (profit 100) takes slot 4, order 2 (profit 80) takes slot 2, order 3 (profit 60) takes the remaining free slot 1.

Order 4 (profit 40) only allows slot 1, which is already taken, so it is rejected.

Total profit is 100 + 80 + 60 = 240 from 3 accepted orders.

Sample Testcase 1
Testcase Input
3
50 1
50 2
50 3
Testcase Output
150 3
Explanation

All three orders have distinct deadlines that exactly match the number of orders, so every one fits into its own slot.

Processing order does not matter here since all profits are equal.

Every order is accepted, giving total profit 150 from 3 orders.