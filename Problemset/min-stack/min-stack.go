
// @Title: 最小栈 (Min Stack)
// @Author: KivenC
// @Date: 2019-07-10 15:21:23
// @Runtime: 32 ms
// @Memory: 7.4 MB

type MinStack struct {
	Stack  []int
	Helper []int
}

/** initialize your data structure here. */
func Constructor() MinStack {
	return MinStack{[]int{}, []int{}}
}

func (this *MinStack) Push(x int) {
	this.Stack = append(this.Stack, x)
	if len(this.Helper) > 0 && this.Helper[len(this.Helper)-1] < x {
		this.Helper = append(this.Helper, this.Helper[len(this.Helper)-1])
    } else {
        this.Helper = append(this.Helper, x)
    }
}

func (this *MinStack) Pop() {
	this.Helper = this.Helper[:len(this.Helper)-1]
	this.Stack = this.Stack[:len(this.Stack)-1]
}

func (this *MinStack) Top() int {
	return this.Stack[len(this.Stack)-1]
}

func (this *MinStack) GetMin() int {
	return this.Helper[len(this.Helper)-1]
}



/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
