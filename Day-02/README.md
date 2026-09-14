*Problem Statement*

Dr. Nisha runs an underwater research station in the Andaman trench, where a chain of acoustic sensors has been bolted onto the seabed to track coral bleaching. The sensors were installed one at a time, each new sensor connected back to exactly one earlier sensor by a fiber-optic tether, so the whole network forms a single branching structure with no loops start anywhere and there is exactly one tether-path to any other sensor. Each tether has a signal-lag rating measured in milliseconds, and the total lag between two sensors is the sum of the lag ratings of every tether on the path connecting them.
Nisha's team wants to run a synchronized measurement sweep, but two sensors can only be paired into the same sweep group if their combined communication lag does not exceed a fixed tolerance D beyond that, the timestamps drift too far apart to be useful. Before scheduling anything, Nisha needs to know exactly how many unordered pairs of sensors qualify for pairing under this tolerance, across the entire network at once, not just locally.
With hundreds of sensors and tethers of wildly different lag ratings, checking every pair directly is exactly the kind of thing her aging dive-computer can't finish before the next data upload window closes. She needs the count computed by exploiting the branching shape of the network itself.

Figure:

                 (1)
                /   \
             2 /     \ 3
              /       \
            (2)       (3)
            /  \        \
         1 /    \ 4      \ 2
          /      \        \
        (4)      (5)      (6)
        
Tether lags shown on each connection. For example, the path from sensor 4 to sensor 6 passes through 2, 1, and 3, accumulating lag 1 + 2 + 3 + 2 = 8.

*Input Format*

The first line contains two integers n and D: the number of sensors and the lag tolerance.
Each of the next n-1 lines contains three integers u, v, w: a tether connecting sensors u and v with lag rating w.

*Output Format*

Print a single integer: the number of unordered sensor pairs (i, j) whose total path lag is at most D.

*Constraints*

2 <= n <= 20000

1 <= w <= 10^6

1 <= D <= 10^12

The sensor network is guaranteed to form a single connected branching structure with no cycles.

Checking every pair directly costs O(n^2), which is far too slow; the intended solution must exploit repeated structural splitting of the network to avoid ever re-examining the same region of sensors from scratch.

*Sample Testcase 0*

*Testcase Input*

6 5
1 2 2
1 3 3
2 4 1
2 5 4
3 6 2

*Testcase Output*
9

*Explanation*

Listing every one of the 15 pairs and their path lags: (1,2)=2, (1,3)=3, (1,4)=3, (1,5)=6, (1,6)=5, (2,3)=5, (2,4)=1, (2,5)=4, (2,6)=7, (3,4)=6, (3,5)=9, (3,6)=2, (4,5)=5, (4,6)=8, (5,6)=11.
Exactly nine of these- (1,2), (1,3), (1,4), (1,6), (2,3), (2,4), (2,5), (3,6), (4,5): do not exceed the tolerance of 5, giving the printed answer.

*Sample Testcase 1*

*Testcase Input*

6 2
1 2 2
1 3 3
2 4 1
2 5 4
3 6 2

*Testcase Output*
3

*Explanation*

With the same network but a stricter tolerance of 2, only the three shortest pairs from the list above still qualify: (1,2)=2, (2,4)=1, and (3,6)=2.
Every other pair now exceeds the tolerance, so the count drops sharply from the previous case.

