Problem Statement
Riya spends her field season monitoring a rainforest reserve using a line of motion triggered camera traps strung along the ridge trail. Whenever a trap fires, it sends a short message to her tablet naming the species it detected, and these messages pile up in the order they arrive throughout the day. Riya does not read every single message herself; instead, at scattered moments during the day she asks her tablet for a quick snapshot of which species have been drawing the most attention so far, so she can radio an update to the ranger team before they move to the next checkpoint.

Each snapshot should list a fixed number of species, ranked from the one sighted most often down to the one sighted least often among the top group, using everything recorded up to that exact moment. Whenever two species have appeared exactly the same number of times, the one whose name comes first alphabetically should be listed first. If fewer distinct species have been observed than the snapshot size requires, the snapshot simply lists all of them that exist so far.

Because sightings and snapshot requests are interleaved unpredictably, and a single field day can generate a very large number of messages, Riya needs the tablet to answer each snapshot request almost instantly rather than rescanning the whole day's log every time. She has asked you to build the logic that powers this live snapshot feature, processing the stream of trap messages and request moments exactly as they occur, one after another, and producing the requested species list the instant each snapshot is asked for.

Species names consist only of lowercase letters and never repeat with different spellings.

Input Format
The first line contains two integers n and C, the number of stream entries and the snapshot size.
Each of the next n lines contains either:
           S name: a sighting of the given species, or

           R: a snapshot request.

Output Format
For every R entry, output one line containing the requested species names, separated by single spaces, in the required order.

Constraints
1 ≤ n ≤ 200000

1 ≤ C ≤ 10

Species names consist of 1 to 15 lowercase English letters.

At least one R entry is guaranteed to appear at some point in the stream.

Sample Testcase 0
Testcase Input
7 2
S dog
S cat
S bat
R
S cat
S cat
R
Testcase Output
bat cat
cat bat
Explanation

After the first three sightings, dog, cat, and bat all have count 1, so ties break alphabetically, giving bat then cat.

Two more cat sightings raise cat to count 3.

The second snapshot now has cat first (count 3), followed by a tie between bat and dog at count 1, broken alphabetically in favor of bat.

dog never appears in either snapshot because the requested size is only 2.

Sample Testcase 1
Testcase Input
8 2
S owl
S owl
S fox
R
S fox
S fox
R
S owl
Testcase Output
owl fox
fox owl
Explanation

After the first three sightings, owl has count 2 and fox has count 1, so the first snapshot lists owl then fox.

Two more fox sightings follow, raising fox to count 3 while owl stays at 2.

The second snapshot now ranks fox ahead of owl since 3 beats 2.

The final owl sighting occurs after the last request, so it has no effect on the output.
