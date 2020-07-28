
| English | [简体中文](README.md) |

# [面试题 17.13. Re-Space LCCI](https://leetcode-cn.com/problems/re-space-lcci/)

## Description

<p>Oh, no! You have accidentally removed all spaces, punctuation, and capitalization in a lengthy document. A sentence like &quot;I reset the computer. It still didn&#39;t boot!&quot; became &quot;iresetthecomputeritstilldidntboot&#39;&#39;. You&#39;ll deal with the punctuation and capi&shy;talization later; right now you need to re-insert the spaces. Most of the words are in a dictionary but a few are not. Given a dictionary (a list of strings) and the document (a string), design an algorithm to unconcatenate the document in a way that minimizes the number of unrecognized characters. Return the number of unrecognized characters.</p>

<p><strong>Note: </strong>This&nbsp;problem is slightly different from the original one in the book.</p>

<p>&nbsp;</p>

<p><strong>Example: </strong></p>

<pre>
<strong>Input: </strong>
dictionary = [&quot;looked&quot;,&quot;just&quot;,&quot;like&quot;,&quot;her&quot;,&quot;brother&quot;]
sentence = &quot;jesslookedjustliketimherbrother&quot;
<strong>Output: </strong> 7
<strong>Explanation: </strong> After unconcatenating, we got &quot;<strong>jess</strong> looked just like <strong>tim</strong> her brother&quot;, which containing 7 unrecognized characters.
</pre>

<p><strong>Note: </strong></p>

<ul>
	<li><code>0 &lt;= len(sentence) &lt;= 1000</code></li>
	<li><code><font face="sans-serif, Arial, Verdana, Trebuchet MS">The total number of characters in&nbsp;</font>dictionary</code>&nbsp;is less than or equal to 150000.</li>
	<li>There are only lowercase letters in&nbsp;<code>dictionary</code>&nbsp;and&nbsp;<code>sentence</code>.</li>
</ul>


## Related Topics

- [Memoization](https://leetcode-cn.com/tag/memoization)
- [String](https://leetcode-cn.com/tag/string)

## Similar Questions


