
| [English](README_EN.md) | 简体中文 |

# [75. 颜色分类](https://leetcode-cn.com/problems/sort-colors/)

## 题目描述

<p>给定一个包含红色、白色和蓝色，一共&nbsp;<em>n </em>个元素的数组，<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a></strong>对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。</p>

<p>此题中，我们使用整数 0、&nbsp;1 和 2 分别表示红色、白色和蓝色。</p>

<p><strong>注意:</strong><br>
不能使用代码库中的排序函数来解决这道题。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [2,0,2,1,1,0]
<strong>输出:</strong> [0,0,1,1,2,2]</pre>

<p><strong>进阶：</strong></p>

<ul>
	<li>一个直观的解决方案是使用计数排序的两趟扫描算法。<br>
	首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。</li>
	<li>你能想出一个仅使用常数空间的一趟扫描算法吗？</li>
</ul>


## 相关话题

- [排序](https://leetcode-cn.com/tag/sort)
- [数组](https://leetcode-cn.com/tag/array)
- [双指针](https://leetcode-cn.com/tag/two-pointers)

## 相似题目

- [排序链表](../sort-list/README.md)
- [摆动排序](../wiggle-sort/README.md)
- [摆动排序 II](../wiggle-sort-ii/README.md)
