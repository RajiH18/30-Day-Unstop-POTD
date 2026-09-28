Problem Statement
Riya coordinates the central dispatch desk at a busy city hospital. Throughout her shift, requests for urgent supplies arrive from different wards, each carrying a unique request number and a severity level assigned by the attending doctor. A higher severity number means the patient needs the supply more urgently. Riya's desk does not always serve requests in the order they arrive: whenever a runner becomes free, the desk must hand over the single pending request with the highest severity, and if several pending requests share the same highest severity, the one that reached the desk earliest must be chosen, since it has already been waiting longest.

Wards occasionally call back to say a patient's condition has changed, in which case the severity of an already pending (not yet served) request is revised, while its original place in the waiting order stays unchanged, since it is still the same request. A ward may also cancel a request outright if the issue resolves on its own; a cancelled request must never be handed to a runner. Riya wants a system that processes a long log of such arrivals, revisions, cancellations, and runner hand offs, always reporting who is served next the moment a runner arrives, or reporting that nobody is currently waiting.

Given the volume of requests during a shift, Riya cannot manually rescan every pending request each time a runner appears; the log must be processed as it happens, in order, and each hand off must be resolved using only the requests that are still valid and unclaimed at that exact moment. Revisions and cancellations may refer to requests that have already been served, in which case they should simply have no effect.

Input Format
The first line contains an integer q, the number of log lines. Each of the next q lines contains one of the following:
"ADD id priority" (a new request numbered id with the given priority arrives)
"UPDATE id priority" (the severity of pending request id changes)
"CANCEL id" (pending request id is withdrawn)
"DISPATCH" (a runner becomes free)
Output Format
For every DISPATCH line, print the id served, or -1 if no request is currently pending, each on its own line.

Constraints
1 <= q <= 2*10^5

1 <= id <= 10^9 (ids are distinct across ADD lines)

1 <= priority <= 10^9

Sample Testcase 0
Testcase Input
5
ADD 1 3
ADD 2 3
UPDATE 2 3
DISPATCH
DISPATCH
Testcase Output
1
2
Explanation

Requests 1 and 2 both have priority 3, and request 1 arrived first.

UPDATE 2 3 keeps request 2's priority the same and does not change its arrival position.

The tie between equal priorities is broken by arrival order, so request 1 is served first.

Request 2 is served next since it is the only one left.

Sample Testcase 1
Testcase Input
7
ADD 101 5
ADD 102 9
DISPATCH
ADD 103 9
DISPATCH
CANCEL 103
DISPATCH
Testcase Output
102
103
101
Explanation

After the first two ADD lines, requests 101 (priority 5) and 102 (priority 9) are pending.

The first DISPATCH picks 102 since it has the higher priority.

Request 103 arrives with priority 9, ties nothing since 102 is gone, so the second DISPATCH serves 103.

CANCEL 103 has no effect since 103 was already served; the last DISPATCH serves the only remaining request, 101.