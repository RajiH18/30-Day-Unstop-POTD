Problem Statement
Vihaan manages the module network aboard an orbiting research station. The station has n modules, and engineers have surveyed m possible corridors that could each be built between two modules, every corridor carrying a construction cost representing crew-hours and material. No corridor has been built yet in this exercise; Vihaan is planning which budget levels would allow which modules to reach each other.

Mission control keeps sending him budget scenarios: given two modules and a spending ceiling, Vihaan must say whether those two modules could be made mutually reachable if the station only ever built corridors whose individual cost does not exceed that ceiling using as many such affordable corridors as needed, in any combination, since cost is the only restriction and connections can pass through any number of intermediate modules.

Each scenario is independent of the others; a ceiling of one value does not carry over to the next question, and Vihaan always considers the full set of corridors whose cost fits under that scenario's ceiling. Because the station's engineering log lists corridors in a fairly arbitrary order and mission control's scenarios arrive with wildly different ceilings, Vihaan cannot re-examine every corridor from scratch each time the station's uplink bandwidth is precious and a fast answer is needed for every scenario in the batch he receives.

Help Vihaan process the whole batch of scenarios and answer each one with a simple yes-or-no about reachability, without wasting station resources.

Input Format
Line 1: three integers n, m, q.
Each of the next m lines: three integers u, v, cost describing one possible corridor.
Each of the next q lines: three integers a, b, budget describing one scenario.
Output Format
Print q lines. For the i-th scenario, print "YES" if modules a and b could be made mutually reachable using only corridors of cost at most budget, otherwise print "NO".

Constraints
1 ≤ n ≤ 10^5

1 ≤ m, q ≤ 10^5

1 ≤ u, v, a, b ≤ n

1 ≤ cost, budget ≤ 10^9

Sample Testcase 0
Testcase Input
5 4 3
1 2 2
2 3 2
2 4 5
1 5 5
1 3 2
4 5 2
1 5 9
Testcase Output
YES
NO
YES
Explanation

Ceiling 2 admits corridors 1-2 and 2-3, linking modules 1, 2 and 3, so module 1 reaches module 3.

Ceiling 2 does not admit corridors 2-4 and 1-5 (both cost 5), so modules 4 and 5 stay apart.

Ceiling 9 admits all four corridors, linking everything through corridor 1-5, so module 1 reaches module 5.

Sample Testcase 1
Testcase Input
4 3 2
1 2 5
2 3 10
3 4 1
1 3 10
1 4 4
Testcase Output
YES
NO
Explanation

For ceiling 10, every corridor (costs 5, 10, 1) qualifies, linking modules 1-2-3-4, so module 1 reaches module 3.

For ceiling 4, only the corridor 3-4 (cost 1) qualifies; corridors costing 5 and 10 are excluded.

Under ceiling 4, module 1 is isolated from module 4, since no affordable corridor touches module 1.

The two scenarios are evaluated independently, using only corridors within each one's own ceiling.
