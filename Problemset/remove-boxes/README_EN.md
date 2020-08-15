
| English | [简体中文](README.md) |

# [546. Remove Boxes](https://leetcode-cn.com/problems/remove-boxes/)

## Description

<p>Given several boxes with different colors represented by different positive numbers.<br />
You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (composed of k boxes, k &gt;= 1), remove them and get <code>k*k</code> points.<br />
Find the maximum points you can get.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> boxes = [1,3,2,2,2,3,4,3,1]
<strong>Output:</strong> 23
<strong>Explanation:</strong>
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----&gt; [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----&gt; [1, 3, 3, 3, 1] (1*1=1 points) 
----&gt; [1, 1] (3*3=9 points) 
----&gt; [] (2*2=4 points)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= boxes.length &lt;= 100</code></li>
	<li><code>1 &lt;= boxes[i]&nbsp;&lt;= 100</code></li>
</ul>


## Related Topics

- [Depth-first Search](https://leetcode-cn.com/tag/depth-first-search)
- [Dynamic Programming](https://leetcode-cn.com/tag/dynamic-programming)

## Similar Questions

- [Strange Printer](../strange-printer/README_EN.md)
