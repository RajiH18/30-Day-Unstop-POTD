## Problem Statement

Kabir coaches middle-distance runners at a regional athletics academy. His star sprinter Nisha wears a wrist tracker during every training run that records her speed, in km/h, once every second, giving a long sequence of `n` readings for the session.

Kabir's coaching philosophy is that raw top speed matters less than pacing discipline a runner who holds a steady effort for a long stretch is developing better race control than one who bursts and stalls. He defines a stretch of the session as "steady" if, across every second in that stretch, the fastest moment and the slowest moment never differ by more than a tolerance `L` that he sets based on the runner's fitness level. Wider swings than that mean Nisha was either sprinting recklessly or coasting, both of which break the "steady effort" label.

After every session, Kabir scrolls through the second-by-second data by hand looking for the longest steady stretch to highlight in his training notes, but with sessions running to tens of thousands of readings, he wants this automated. Given the full list of speed readings and his chosen tolerance `L`, he wants the length, in seconds, of the longest continuous stretch of the session during which Nisha's pace stayed within that tolerance of itself.

#### Input Format

- Line 1: two integers `n` and `L:` the number of readings and the tolerance.
- Line 2: `n` integers: the speed readings in order.

#### Output Format

Print a single integer: the length of the longest steady stretch.

#### Constraints

- 1 <= n <= 200000
- 0 <= speed[i] <= 10^9
- 0 <= L <= 10^9

#### Sample Testcase 0

#### Testcase Input

7 3 10 12 11 13 20 21 19

#### Testcase Output

4

#### Explanation

- The stretch of the first four readings `[10, 12, 11, 13]` has a maximum of `13` and a minimum of `10`, a spread of exactly `3`, which is still within tolerance.
- Including the fifth reading `20` would make the spread `10`, well past the tolerance, so that stretch must break there.
- After the break, `[20, 21, 19]` has a spread of only `2`, but its length is just `3`.
- The longest steady stretch across the whole session is therefore `4`.

#### Sample Testcase 1

#### Testcase Input

5 0 5 5 5 8 8

#### Testcase Output

3

#### Explanation

- With tolerance `0`, only perfectly flat stretches count, since even a spread of `1` would break steadiness.
- The first three readings are all exactly `5`, giving a steady stretch of length `3`.
- The last two readings are both `8`, giving a steady stretch of length `2`, which is shorter.
- The longest steady stretch overall is `3`.