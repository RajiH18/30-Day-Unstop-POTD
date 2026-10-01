Problem Statement
Meera works in the planning office of Meridian, a rapidly expanding smart city where every district is identified by a short code such as D1 or GH7. Each district starts out with its own energy efficiency rating, a number reflecting how well its infrastructure currently performs. As the city grows, engineering teams gradually lay fiber links between pairs of districts, and once two districts are linked directly or through a chain of other links, they are considered part of the same operating zone and begin sharing resources and monitoring dashboards.

Meera's office receives a long stream of updates through the season. Sometimes a new fiber link is completed between two named districts, merging their zones if they were not already connected. Sometimes an individual district receives an infrastructure investment that raises its own rating by a given amount, independent of any other district in its zone. At various points, a city council member asks Meera for the current highest efficiency rating found anywhere within a specific district's zone, since that number is used to decide which zone should host the next regional showcase.

Because links only ever join zones together and investments only ever raise a rating, Meera never needs to handle a zone splitting apart or a rating decreasing. Still, with hundreds of thousands of updates arriving over the season and district codes referenced by name rather than by a convenient index, she needs a way to resolve each investment and each showcase question quickly, using only the zone information collected so far, without ever rescanning every district in a zone from scratch.

Input Format
The first line contains an integer n, the number of districts.
Each of the next n lines contains a district code (a string) and its initial rating.
The next line contains an integer q, the number of events.
Each of the next q lines is one of:
"LINK X Y" (a fiber link joins the zones containing districts X and Y)
"BOOST X V" (district X's rating increases by V)
"QUERY X" (report the highest rating currently in district X's zone)
Output Format
For every QUERY event, print the requested value on its own line.

Constraints
1 <= n <= 210^5

1 <= q <= 210^5

District codes are distinct strings of up to 15 alphanumeric characters

1 <= initial rating <= 10^9

1 <= V <= 10^9

Sample Testcase 0
Testcase Input
4
D1 50
D2 30
D3 70
D4 10
6
QUERY D3
LINK D1 D2
BOOST D2 40
QUERY D1
LINK D3 D4
QUERY D4
Testcase Output
70
70
70
Explanation

D3 is alone in its zone at first, so its top rating is simply 70.

Linking D1 and D2 forms a zone with ratings {50,30}; boosting D2 by 40 makes it 70, so the zone's top becomes 70.

Linking D3 and D4 forms a zone with ratings {70,10}, so its top stays 70.

Sample Testcase 1
Testcase Input
3
D1 5
D2 100
D3 20
5
QUERY D2
BOOST D1 200
QUERY D1
LINK D1 D3
QUERY D3
Testcase Output
100
205
205
Explanation

D2 starts alone with rating 100.

Boosting D1 by 200 raises it from 5 to 205, so its own zone's top becomes 205.

Linking D1 and D3 merges zones {205} and {20}, keeping the top at 205 for both codes.