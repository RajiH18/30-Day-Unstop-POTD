## Problem Statement

Dr. Ishaan Verma monitors a chain of deep space relay beacons for the Anantara Array, a listening post built to catch faint calibration pulses from interstellar probes drifting past the outer system. Each beacon, once active, continuously broadcasts a signature code, a non negative integer that identifies its current calibration state. Over the course of a long shift, beacons power on, power down, and technicians occasionally need to run a cross check between a code they are about to assign and whichever active beacon differs from it the most, bit for bit, since a large bitwise difference (the XOR of the two codes) indicates that pair is best suited for a stress calibration test that afternoon.

Beacons are identified by unique station numbers, and a station number may be reused later in the shift once its beacon has powered down. When a beacon powers on, it is assigned a fresh signature code and remains active, continuing to broadcast exactly that code, until a technician explicitly powers it down. Several beacons may hold the same numeric code at once, since entire manufacturing batches ship with identical firmware defaults; when a cross check is requested, Ishaan only needs to report the resulting deviation value together with the station number of any one currently active beacon that achieves it, and If several active beacons achieve the same maximal deviation, report the beacon with the smallest station ID.

Across a single shift Ishaan logs three kinds of moments, in the exact order they occurred: a beacon powering on with a given code, a beacon powering down, and a cross check request against a code a technician is about to commit to next. At the start of the shift no beacons are active. It is guaranteed that a beacon is never powered on twice without first powering down, is never powered down while already inactive, and that every cross check request occurs while at least one beacon is active somewhere on the array.

Given the full log of a shift, help Ishaan produce, for every cross check moment, the maximal deviation value together with a witness station number, so the technicians know exactly which pairing to schedule next.

#### Input Format

- Line 1: an integer M, the number of log entries.
- Each of the next M lines is one of:
  `ON id code`
  `OFF id`
  `CHECK code`

#### Output Format

For every `CHECK` entry, print two integers on their own line: the maximal deviation value and the witness station number.

#### Constraints

- 1 <= M <= 2 x 10^5
- 1 <= id <= 2 x 10^5
- 0 <= code < 2^20
- The log is well formed as described above.

#### Sample Testcase 0

#### Testcase Input

5 ON 12 27 ON 7 14 CHECK 9 OFF 12 CHECK 3

#### Testcase Output

18 12 13 7

#### Explanation

- After the two ON entries, beacons 12 (code 27) and 7 (code 14) are both active.
- Comparing 9 against 27 gives 18, and against 14 gives 7, so 18 with witness 12 is reported.
- Beacon 12 then powers down, leaving only beacon 7 active.
- Comparing 3 against the sole remaining code 14 gives 13, reported with witness 7.

#### Sample Testcase 1

#### Testcase Input

10 ON 10 7 ON 4 25 ON 15 18 CHECK 5 ON 2 28 CHECK 3 OFF 4 CHECK 3 OFF 2 CHECK 3

#### Testcase Output

28 4 31 2 31 2 17 15

#### Explanation

- For `CHECK 5`, the maximum XOR is `5 XOR 25 = 28`, so station `4` is selected.
- After station `2` with code `28` is activated, `CHECK 3` gives `3 XOR 28 = 31`, so station `2` is selected.
- After stations `4` and `2` are powered down, only codes `7` and `18` remain; `3 XOR 18 = 17` is maximum, so station `15` is selected.