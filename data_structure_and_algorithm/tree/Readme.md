

![image](https://user-images.githubusercontent.com/46132312/152686914-03c608d2-448d-413d-b6bd-1d6cf16b9ae5.png)

Custom testcase
[8,3,10,1,6, null, 14, null, null, 4, 7,13, null]

<h2> Algorithm - Part 1 </h2>

1. Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree.

- result for the above tree is [8, 3, 1,6 ,4,7, 10, 14, 13]

2. In-order traversal is to traverse the left subtree first. then vist the root. Finally, traverse the right subtree.

- result for the above tree is [1,3,4,6,7,8,10,13,14]

3. Post-order traversal is to traverse the left subtree first. Then traverse the right subtree. Finally , visit the node.

- result for the above tree is [1,4,7,6,3,13,14,10,8]

<h2> Compexity Analysis </h2>

The time complexity for both iterative solution and recursive solution is O(N)

The space complexity for iterative solution is O(N). On the other hand, if we take system stack into consideration, the space complexity is O(N) as well

To be cautious , if the depth of tree is too large and recursive solution is used, we might suffer from **stack overflow** problem.

<h2> Algorithm - Part 2 </h2>

4. Breadth-First Search is an algorithm to traverse or search in data structure like a tree or a graph. The algorithm starts with a root node and visit the node first.
Then traverse it neighbor, traverse its second leve neighbors , so on and so forth

- result for the above tree is [[8],[3,10],[1,6,14],[4,7,13]]


