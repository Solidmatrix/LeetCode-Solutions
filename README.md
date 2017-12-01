# LeetCode-in-Python

## 218. The Skyline Problem
法1：遍历buildings，储存所有端点。遍历buildings，更新端点的高度。最坏情况下复杂度为O(N2)。不可取。

法2：对buildings按高度从大到小排序（这样端点的高度就不需要更新），复杂度为O(NlogN)。建立数组保存高度为0的区间（初始为[0, maxint]）并遍历buildings。对每一个building找到端点在哪两个区间中，并删除这两个区间之间所有的区间。在第K次遍历时，高度为0的区间最多有K个，采用二分搜索的的复杂度为O(logK)。因此最坏情况下整体复杂度为O(NlogN)。已达到最优时间复杂度。

## 238. Product of Array Except Self
要求不能用除法运算。因此分别计算出某一元素左边和右边的元素之积，再将这两者相乘。复杂度为O(3N)=O(N)。
