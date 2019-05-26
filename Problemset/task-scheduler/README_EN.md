
| English | [简体中文](README.md) |

# [0621. Task Scheduler](https://leetcode-cn.com/problems/task-scheduler/)

## Description

<p>Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.</p>

<p>However, there is a non-negative cooling interval <b>n</b> that means between two <b>same tasks</b>, there must be at least n intervals that CPU are doing different tasks or just be idle.</p>

<p>You need to return the <b>least</b> number of intervals the CPU will take to finish all the given tasks.</p>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> tasks = [&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;], n = 2
<b>Output:</b> 8
<b>Explanation:</b> A -&gt; B -&gt; idle -&gt; A -&gt; B -&gt; idle -&gt; A -&gt; B.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The number of tasks is in the range [1, 10000].</li>
	<li>The integer n is in the range [0, 100].</li>
</ol>


## Related Topics

- [Greedy](https://leetcode-cn.com/tag/greedy)
- [Queue](https://leetcode-cn.com/tag/queue)
- [Array](https://leetcode-cn.com/tag/array)

## Similar Questions

- [Rearrange String k Distance Apart](../rearrange-string-k-distance-apart/README_EN.md)
- [Reorganize String](../reorganize-string/README_EN.md)
