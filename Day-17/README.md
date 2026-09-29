Problem Statement
Aarav manages a chain of motion sensors placed along a single forest trail inside a wildlife reserve. Every hour, each sensor records one footprint reading: a count value describing how strong the disturbance was, together with a species code identifying which animal most likely triggered it. Over n consecutive hours, Aarav collects one such pair of numbers per hour, in order.

For his weekly report, Aarav studies the trail in fixed stretches of k consecutive hours at a time, sliding this stretch forward one hour at a step, so that stretch two starts one hour after stretch one, and so on until the stretch reaches the end of the log. For each stretch, Aarav first checks whether the stretch shows healthy species variety: he counts how many different species codes appear anywhere within it, and considers the stretch "notable" only when that count of distinct species is at least half of the stretch length, rounding down requirements in the natural way (twice the distinct count must be at least the stretch length). A stretch dominated by a single repeating species, with almost no other animals passing through, is not notable and gets skipped in the report.

For every notable stretch, Aarav wants to record the single loudest reading observed anywhere inside it, since a very strong disturbance close to a period of high variety often points to a rare event worth investigating further, such as a predator passing through. For stretches that are not notable, he simply records that nothing is worth flagging. Because the trail log can span an entire season and Aarav needs the whole report before submitting it, he needs every stretch resolved in a single pass over the readings rather than by rechecking each stretch from scratch.

Input Format
The first line contains two integers n and k.
The second line contains n integers, the footprint readings v_1 ... v_n.
The third line contains n integers, the species codes s_1 ... s_n.
Output Format
Print n - k + 1 integers separated by single spaces, in order, one for each stretch: the loudest reading in that stretch if it is notable, or -1 otherwise.

Constraints
1 <= k <= n <= 2*10^5

1 <= v_i <= 10^9

1 <= s_i <= 10^9

Sample Testcase 0
Testcase Input
6 3
5 3 5 8 8 2
10 20 10 30 20 40
Testcase Output
5 8 8 8
Explanation

Stretch [5,3,5] has species {10,20,10}: 2 distinct species, and 2*2 >= 3, so it is notable; loudest reading is 5.

Stretch [3,5,8] has species {20,10,30}: 3 distinct, notable; loudest reading is 8.

Stretch [5,8,8] has species {10,30,20}: 3 distinct, notable; loudest reading is 8.

Stretch [8,8,2] has species {30,20,40}: 3 distinct, notable; loudest reading is 8.

Sample Testcase 1
Testcase Input
5 4
4 6 2 9 5
1 1 1 1 2
Testcase Output
-1 9
Explanation

Stretch [4,6,2,9] has only species 1 throughout: 1 distinct species, and 2*1 < 4, so it is not notable, giving -1.

Stretch [6,2,9,5] has species {1,1,1,2}: 2 distinct species, and 2*2 >= 4, so it is notable; loudest reading is 9.