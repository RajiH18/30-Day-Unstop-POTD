Problem Statement
Kabir supervises cataloguing at the Kestrel excavation site. Every shard unearthed is stamped with a code made of lowercase letters, and Kabir assigns each shard a numeric era tag based on the soil layer it came from. Over the course of a season, events arrive one after another: sometimes a freshly cleaned shard is registered with its code and era, and sometimes a visiting scholar asks a question about the catalogue so far.

A scholar's question names a code prefix and an era number, and wants to know how many registered shards have a code beginning with that exact prefix and carrying that exact era tag. Because two shards can share a prefix while coming from completely different soil layers, and because eras are not small tidy numbers but can be any large identifier used by the site's dating lab, Kabir cannot simply keep one running total he needs the count broken down precisely by both the textual beginning of the code and the era it belongs to, answered the moment each question is asked, using only the shards registered before that point.

The registrations and questions are interleaved in the order they happen, and Kabir must answer each question immediately, without waiting for the season to end. Help him build the running catalogue and answer every scholar's question as it comes in.

Input Format
Line 1: an integer Q, the number of events.
Each of the next Q lines is one of:
ADD code era: register a shard with the given code and era.
QUERY prefix era: ask how many registered shards have a code starting with the given prefix and the given era.
Output Format
For every QUERY event, print the requested count on its own line, in the order the queries appear.

Constraints
1 ≤ Q ≤ 2×10^5

codes and prefixes consist of lowercase English letters only

the sum of the lengths of all codes and prefixes over the whole input ≤ 2×10^5

1 ≤ era ≤ 10^9

Sample Testcase 0
Testcase Input
4
ADD cat 5
ADD car 5
QUERY ca 9
QUERY do 5
Testcase Output
0
0
Explanation

Both registered shards use era 5, none use era 9, so the first query answers 0.

No shard code begins with "do" at all, so the second query answers 0 regardless of era.

Sample Testcase 1
Testcase Input
5
ADD gold 1
ADD gods 1
ADD golf 2
QUERY go 1
QUERY gol 2
Testcase Output
2
1
Explanation

Shards "gold" and "gods" both start with "go" and both carry era 1, so the first query answers 2.

Shard "golf" also starts with "go" but carries era 2, so it does not count for the first query.

Only "golf" starts with "gol" and carries era 2, so the second query answers 1.

"gold" starts with "gol" too but its era is 1, not 2, so it is excluded.
