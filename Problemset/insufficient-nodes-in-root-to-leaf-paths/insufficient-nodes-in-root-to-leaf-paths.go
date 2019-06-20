
// @Title: 根到叶路径上的不足节点 (Insufficient Nodes in Root to Leaf Paths)
// @Author: KivenC
// @Date: 2019-06-20 10:23:48
// @Runtime: 128 ms
// @Memory: 10.1 MB

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sufficientSubset(root *TreeNode, limit int) *TreeNode {
	return Dfs(root, 0, limit)
}

// 后序遍历
func Dfs(node *TreeNode, value int, limit int) *TreeNode {
	if node.Left == nil && node.Right == nil {
		if node.Val+value < limit {
			return nil
		}
		return node
	}
    
	var left, right *TreeNode
	if node.Left != nil {
		left = Dfs(node.Left, value+node.Val, limit)
	}
	if node.Right != nil {
		right = Dfs(node.Right, value+node.Val, limit)
	}
    
	if left == nil && right == nil {
		return nil
	}
	node.Left, node.Right = left, right
	return node
}

