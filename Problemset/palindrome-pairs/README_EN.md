
| English | [简体中文](README.md) |

# [336. Palindrome Pairs](https://leetcode-cn.com/problems/palindrome-pairs/)

## Description

<p>Given a list of <b>unique</b> words, find all pairs of <b><i>distinct</i></b> indices <code>(i, j)</code> in the given list, so that the concatenation of the two words, i.e. <code>words[i] + words[j]</code> is a palindrome.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;abcd&quot;,&quot;dcba&quot;,&quot;lls&quot;,&quot;s&quot;,&quot;sssll&quot;]</span>
<strong>Output: </strong><span id="example-output-1">[[0,1],[1,0],[3,2],[2,4]] 
<strong>E</strong></span><strong>xplanation<span>: </span></strong>The palindromes are <code>[&quot;dcbaabcd&quot;,&quot;abcddcba&quot;,&quot;slls&quot;,&quot;llssssll&quot;]</code>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[&quot;bat&quot;,&quot;tab&quot;,&quot;cat&quot;]</span>
<strong>Output: </strong><span id="example-output-2">[[0,1],[1,0]] 
</span><span id="example-output-1"><strong>E</strong></span><strong>xplanation<span>: </span></strong>The palindromes are <code>[&quot;battab&quot;,&quot;tabbat&quot;]</code>
</pre>
</div>
</div>


## Related Topics

- [Trie](https://leetcode-cn.com/tag/trie)
- [Hash Table](https://leetcode-cn.com/tag/hash-table)
- [String](https://leetcode-cn.com/tag/string)

## Similar Questions

- [Longest Palindromic Substring](../longest-palindromic-substring/README_EN.md)
- [Shortest Palindrome](../shortest-palindrome/README_EN.md)
