Problem Statement
Dev's college robotics team is prepping for the regional build-off, where their conveyor rig feeds spare components one at a time onto a moving belt. Each component is labeled with a single capital letter marking its type (motors, sensors, gears, and so on), and the belt only moves in one direction once a component passes Dev's station, he cannot pull it back to grab it later.

To assemble their competition gadget, the team needs a specific kit: a minimum required count of each of several component types, all grabbed together in one motion since the rig only allows a single continuous grab across consecutive belt positions. Dev can start his grab at any point on the belt and end it at any later point, but everything between the start and end of the grab gets scooped up together, useful parts and duplicates alike.

Given the exact sequence of component types that will pass down the belt today, and the kit requirements handed to him by his teammate, Dev wants to know the shortest possible continuous grab the fewest consecutive belt positions that would still contain at least the required number of every needed component type. If the belt simply never carries enough of some required type in total, no grab can ever complete the kit, and Dev needs to know that too so the team can order the part separately instead of waiting on the belt.

Input Format
Line 1: two integers n and m: the belt length and the number of distinct required component types.
Line 2: a string of n uppercase letters: the belt sequence in order.
Line 3: m pairs, type count, space-separated: the required minimum count for each needed type.
Output Format
Print a single integer: the length of the shortest valid grab, or -1 if no grab can satisfy all requirements.

Constraints
1 <= n <= 200000

1 <= m <= 26

1 <= count <= n

All belt characters and required types are uppercase letters A–Z.

Sample Testcase 0
Testcase Input
10 2
ABACABBCAA
A 2
B 1
Testcase Output
3
Explanation

The kit needs at least two As and one B in a single contiguous grab.

Positions 1 to 3 give the sequence "ABA", which already contains two As and one B.

Since the kit needs at least three parts in total (two A plus one B), no grab shorter than length 3 could ever satisfy it.

No other stretch of the belt does better, so 3 is the shortest possible grab.

Sample Testcase 1
Testcase Input
5 1
AAAAA
B 1
Testcase Output
-1
Explanation

The kit requires at least one component of type B.

Scanning the entire belt, not a single B ever appears among the five components.

Since the required type never shows up at all, no grab of any length can complete the kit.

The answer is -1.