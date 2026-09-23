Problem Statement
Tomasz Wybicki dispatches flights out of Rzepin Aerodrome, the single home base for a regional charter operator whose aircraft hop between a network of waypoints connected by direct legs. Every direct leg burns a fixed amount of fuel and exposes the aircraft to a fixed amount of turbulence, and both quantities are known in advance from years of recorded flights along that corridor. A full route from the home aerodrome to any other waypoint is simply a sequence of direct legs flown one after another, its total fuel cost the sum of the individual legs' fuel costs, and its total turbulence exposure the sum of the individual legs' turbulence contributions.

Throughout the day, pilots radio in requests before departure. Each request names a destination waypoint together with a turbulence tolerance, the greatest total exposure the pilot is willing to accept for that particular flight, since some pilots carry delicate cargo and set a low tolerance while others are comfortable with a much higher one. Tomasz needs to tell each pilot the least total fuel a route from the home aerodrome to their destination could possibly burn while keeping the accumulated turbulence exposure of that route at or below the stated tolerance. If no such route exists, because every way of reaching that destination exceeds the tolerance or the destination simply cannot be reached at all, Tomasz reports that the flight cannot be dispatched under the stated tolerance.

Rzepin's network has grown busy enough that Tomasz can no longer work these routings out by hand, especially since two requests for the same destination can carry very different tolerances and therefore very different answers. Turbulence tolerances at Rzepin never exceed a small fixed ceiling set by regulation, and no individual leg's turbulence contribution exceeds that same ceiling either, so cumulative exposure along any route worth considering never needs to be tracked past that ceiling. Legs may be flown in only one direction, since the prevailing wind corridor makes the reverse direction impractical, and it is possible for two waypoints to be connected by more than one direct leg with different fuel and turbulence figures, representing different altitude corridors between them.

Given the full network of legs and the day's list of destination and tolerance requests, help Tomasz answer every request in the order it was radioed in.

Input Format
Line 1: three integers n, m, R, the number of waypoints, the number of legs, and the turbulence ceiling.
Each of the next m lines: four integers u v fuel turb, a leg from u to v.
Next line: an integer q, the number of requests.
Each of the next q lines: two integers dest tol, a destination waypoint and a turbulence tolerance
Output Format
For each request, in input order, print the minimum fuel cost, or -1 if the flight cannot be dispatched under the stated tolerance.

Constraints
1 <= n <= 10000

1 <= m <= 30000

0 <= R <= 100

0 <= turb <= R for every leg

1 <= fuel <= 10^9

1 <= q <= 2*10^5

1 <= dest <= n, 0 <= tol <= R

Home aerodrome is waypoint 1.

Sample Testcase 0
Testcase Input
4 5 4
1 2 4 1
2 3 1 2
1 3 10 0
3 4 2 1
2 4 6 3
3
4 2
4 4
3 0
Testcase Output
12
7
10
Explanation

Route 1->3->4 costs 12 fuel with turbulence 1, the only option within tolerance 2, so it answers the first request.

With tolerance 4, route 1->2->3->4 also qualifies at turbulence 4 and costs only 7 fuel, beating the earlier route.

For destination 3 with tolerance 0, only the direct leg 1->3 has zero turbulence, costing 10 fuel.

Sample Testcase 1
Testcase Input
3 1 3
1 2 5 3
3
2 2
2 3
3 3
Testcase Output
-1
5
-1
Explanation

The only route to waypoint 2 has turbulence 3, which exceeds a tolerance of 2, so the first request fails.

Raising the tolerance to exactly 3 makes that same route valid, costing 5 fuel.

Waypoint 3 has no incoming leg at all, so it is unreachable regardless of tolerance.