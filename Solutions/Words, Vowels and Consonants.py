'''Words, Vowels and Consonants 
Given a sentence containing only uppercase/lowercase english alphabets and spaces, you have to count the number of words, vowels and consonants.

Input Format
The first line of input contains T - number of test cases. It's followed by T lines, each line contains a single sentence.

Output Format
For each test case, print the number of words, vowels and consonants, separated by newline.

Constraints
1 <= T <= 1000
1 <= len(sentence) <= 104

Example
Input
4
Hi
Hello World
  Exception  
Hi there

Output
1 1 1
2 3 7
1 4 5
2 3 4

Explanation

Self Explanatory'''
for _ in range(int(input())):
    s=input()
    w=len(s.split())
    vow="aeiouAEIOU"
    v=c=0
    for i in s:
        if i in vow:
            v+=1
        elif i!=" ":
            c+=1
    print(w,v,c)
