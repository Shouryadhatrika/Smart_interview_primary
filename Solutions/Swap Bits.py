'''Swap Bits
Given a number, swap the adjacent bits in the binary representation of the number, and print the new number formed after swapping.

Input Format
The first line of input contains T - the number of test cases. Each of the next T lines contains a number N.

Output Format
For each test case, print the new integer formed after swapping adjacent bits, separated by a new line.

Constraints
1 <= T <= 100000
0 <= N <= 109

Example
Input
4
10
7
43
100

Output
5
11
23
152

Explanation

Test Case-1
Binary Representation of 10: 000...1010
After swapping adjacent bits: 000...0101 (5)

Test Case-2
Binary Representation of 7: 000...0111
After swapping adjacent bits: 000...1011 (11) '''

for i in range(int(input())):
    n=int(input())
    print((n & 0xAAAAAAAA)>>1|(n & 0x55555555)<<1 )
