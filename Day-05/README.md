Problem Statement
Meera is backpacking through an old European city famous for its row of museums lined up along a single cobbled street, one museum per day of her trip. She has exactly n days scheduled in the city, and each day has a fixed entry fee for the museum open that day. Meera cannot skip ahead or revisit she moves through the city street by street, so any stretch of museum visits she picks must be a run of consecutive days.

She has a fixed total travel budget B set aside strictly for museum entry fees, and she wants to spend as many consecutive days as possible touring museums without her cumulative spending on that streak crossing her budget. She can start the streak on any day and end it on any later day, but once she decides to stop for a break, she can't resume the same streak later she just wants to know, looking at her whole itinerary in advance, the longest unbroken run of days she could afford in one go.

Some museums are surprisingly expensive (special exhibits), so it's entirely possible that even a single day's entry fee already exceeds her whole remaining budget, in which case that day simply cannot be the start of any affordable streak.

Meera messages you her day-by-day fee list before she leaves, and wants to know, in advance, the longest such streak she should plan for.

Input Format
Line 1: an integer n and an integer B: the number of days and her total budget.
Line 2: n integers: the entry fee for each day, in order.
Output Format
Print a single integer: the maximum number of consecutive days Meera can tour without her spending on that streak exceeding B.

Constraints
1 <= n <= 200000

1 <= cost[i] <= 10^9

1 <= B <= 10^15

Sample Testcase 0
Testcase Input
6 10
2 1 5 1 1 5
Testcase Output
5
Explanation

Starting from day 1, the running total after each day is 2, 3, 8, 9, 10 for the first five days: exactly 10, still within budget, giving a streak of length 5.

Adding day 6 (+5) would push the total to 15, exceeding the budget of 10, so the streak must stop before it.

Checking other starting points (like days 2–6, which total 13) gives shorter or equally short streaks.

The longest affordable streak is therefore 5 days.

Sample Testcase 1
Testcase Input
4 3
4 4 4 4
Testcase Output
0
Explanation

Every single day already costs 4, which is more than the entire budget of 3.

No streak of even one day can be afforded.

The answer is 0, meaning Meera cannot plan any museum visit within budget.