## Problem Statement

Aarav works the night shift at the Aranya Deep Space Relay Station, where a long-range antenna records signal strength readings from a distant probe once every second. The array is old, and its dish drifts slightly with the station's rotation, so incoming readings can spike or dip sharply due to interference from passing debris.

Mission protocol groups every `k` consecutive seconds of data into one "transmission cycle," and the station log must record the strongest reading observed in each cycle, because that peak is what confirms the probe's signal was actually received above the noise floor. Since the antenna streams data continuously, cycles overlap the first cycle covers seconds `1` to `k`, the second covers seconds `2` to `k+1`, and so on, shifting forward by one second each time, until the last possible cycle ending at the final second of the log.

Aarav has just downloaded tonight's full log of `n` readings, some of which are negative (representing signal dips below the calibrated baseline caused by dust interference). Before he can file his report, he needs the peak value of every overlapping cycle, in order, printed as a single log line so the automated dashboard can plot the “peak trend” for the night shift supervisor.

#### Input Format

- Line 1: two integers `n` and `k:` the number of readings and the cycle length.
- Line 2: `n` integers: the signal readings in the order they were recorded.

#### Output Format

Print `n - k + 1` integers, space-separated, representing the peak reading of each overlapping cycle in order.

#### Constraints

- 1 <= k <= n <= 200000
- -10^9 <= reading[i] <= 10^9

#### Sample Testcase 0

#### Testcase Input

5 2 -3 5 -1 -4 2

#### Testcase Output

5 5 -1 2

#### Explanation

- Cycle `[-3, 5]` peaks at `5`.
- Cycle `[5, -1]` still peaks at `5` since it's still inside the window.
- Cycle `[-1, -4]` peaks at `-1`, the larger of two negative dips.
- Cycle `[-4, 2]` peaks at `2`.

#### Sample Testcase 1

#### Testcase Input

8 3 4 2 12 3 9 5 1 7

#### Testcase Output

12 12 12 9 9 7

#### Explanation

- Cycle `[4, 2, 12]` has its largest value at index 2, so the peak is `12`.
- As the cycle slides forward, `12` stays the peak as long as it remains inside the window (cycles 2 and 3).
- Once index 2 falls outside the window (cycle 4: `[3, 9, 5]`), the peak drops to the next largest value still inside, `9`.
- This continues sliding forward one reading at a time until the log ends, giving `12 12 12 9 9 7`.