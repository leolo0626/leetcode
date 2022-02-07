<h1> Dynamic Programming </h1>

- is a programming paradigm that can systematically and efficiently explore all solutions to problem.

Characteristics : 

1. Break into Overlapping subproblems
2. Optimal substructure 

e.g. Fibonacci sequence has expoential time complexity when we use recursive solution. So we can implement DP algorithm on that

**Remark**

1. divide and conquer break a problem into subproblems, but these subproblems are not overlapping
2. Greedy problems have optimal substructure , but these subproblems are not overlapping

<h2> Ways to implement a DP algorithm </h2>

1. Bottom-up, known as tabulation
- A bottom-up implementation's runtime is usually faster
2. Top-down, also known as memorization
- A top-down implementation is usually much easier to write. 

<h2> Situation should use DP </h2>

If a problem is asking for 
- the maximum/minimum/longest/shortest of something, 
- the number of ways to do something, or if it is possible to reach a certain point,
- it is probably greedy or DP. 

 If you can think of an example where earlier decisions affect future decisions,
 - then DP is applicable.
