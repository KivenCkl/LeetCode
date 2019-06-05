
// @Title: 两数相加 (Add Two Numbers)
// @Author: KivenC
// @Date: 2019-06-05 10:41:01
// @Runtime: 16 ms
// @Memory: 5.2 MB

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
// 	// way 1
// 	var res []ListNode
// 	node1, node2 := l1, l2
// 	tmp := 0
// 	for {
// 		if node1 != nil {
// 			tmp += node1.Val
// 			node1 = node1.Next
// 		}
// 		if node2 != nil {
// 			tmp += node2.Val
// 			node2 = node2.Next
// 		}
// 		res = append(res, ListNode{Val: tmp % 10})
// 		tmp = tmp / 10
// 		if node1 == nil && node2 == nil && tmp == 0 {
// 			break
// 		}
// 	}
// 	for i := len(res) - 1; i > 0; i-- {
// 		res[i-1].Next = &res[i]
// 	}
// 	return &res[0]
    
    // way 2
    resPre := &ListNode{}
	cur := resPre
	carry := 0

	for l1 != nil || l2 != nil || carry > 0 {
		sum := carry

		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}

		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}

		carry = sum / 10

		cur.Next = &ListNode{Val: sum % 10}
		cur = cur.Next
	}
	return resPre.Next   
}

