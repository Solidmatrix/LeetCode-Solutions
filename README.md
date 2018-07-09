# LeetCode Solutions
In Python and C++ and java

## 097. Interleaving String.py
Dynamic programming。O(N^2)。

## 099. Recover Binary Search Tree
前序遍历可以顺序输出BST。可以通过前序遍历找出位置不对的节点。O(N)。

## 123. Best Time to Buy and Sell Stock III
计算出节点i之前的最佳交易和节点i之后的最佳交易。最大获利为所有i交易之和的最大值。O(N)。

## 218. The Skyline Problem
法1：遍历buildings，储存所有端点。遍历buildings，更新端点的高度。最坏情况下复杂度为O(N2)。不可取。

法2：对buildings按高度从大到小排序（这样端点的高度就不需要更新），复杂度为O(NlogN)。建立数组保存高度为0的区间（初始为[0, maxint]）并遍历buildings。对每一个building找到端点在哪两个区间中，并删除这两个区间之间所有的区间。在第K次遍历时，高度为0的区间最多有K个，采用二分搜索的的复杂度为O(logK)。因此最坏情况下整体复杂度为O(NlogN)。已达到最优时间复杂度。O(NlogN)。

## 233. Number of Digit One
Double counting.用双计数法数每一位上1的数量。O(N)其中N是位数。

## 238. Product of Array Except Self
要求不能用除法运算。因此分别计算出某一元素左边和右边的元素之积，再将这两者相乘。O(N)。

## 438. Find All Anagrams in a String.py
和049. Group Anagrams方法类似
