"""
Task
The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
1, 2, 3....n

Note that "....." represents the consecutive values in between.

Example
n = 5

Print the string 12345.

Input Format
The first line contains an integer n.

Constraints
1 <= n <= 150

Output Format
Print the list of integers from 1 through n as a string, without spaces.
"""

#Solution

n = int(input(""))
i = 1
while i <= n:
    print(i, end="")
    i = i+1
