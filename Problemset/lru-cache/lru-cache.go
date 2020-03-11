
// @Title: LRU缓存机制 (LRU Cache)
// @Author: KivenC
// @Date: 2019-07-10 19:24:07
// @Runtime: 172 ms
// @Memory: 15.5 MB

// 双链表
type ListNode struct {
	Key   int
	Value int
	Prev  *ListNode
	Next  *ListNode
}

type LRUCache struct {
	Mapper map[int]*ListNode
	Cap    int
	Head   *ListNode
	Tail   *ListNode
}

func Constructor(capacity int) LRUCache {
	m := make(map[int]*ListNode, capacity)
	h, t := &ListNode{}, &ListNode{}
	// 连接头尾哨兵结点
    h.Next = t
	t.Prev = h
	return LRUCache{
		Mapper: m,
		Cap:    capacity,
		Head:   h,
		Tail:   t,
	}
}

func (this *LRUCache) Get(key int) int {
	if v, ok := this.Mapper[key]; ok {
        // 如果 key 在 Mapper 中，则将其挪至尾结点，并返回其值
		this.MoveToTail(v.Key, v.Value)
		return v.Value
	} else {
		return -1
	}
}

func (this *LRUCache) Put(key int, value int) {
	if v, ok := this.Mapper[key]; ok {
        // 如果 key 在 Mapper 中，则更新其值，并将其挪至尾结点
		v.Value = value
		this.MoveToTail(v.Key, v.Value)
	} else {
		if len(this.Mapper) == this.Cap {
            // 如果缓存容量达到上限，则删除头结点
			delete(this.Mapper, this.Head.Next.Key)
			this.Head.Next = this.Head.Next.Next
			this.Head.Next.Prev = this.Head
		}
        // 将该键值对挪至尾节点
        this.MoveToTail(key, value)
	}
}

// 如果该键值对存在于 Mapper 中，则其提出，插入至尾结点
// 如果该键值对不存在，那么创建一个新结点，插入至尾结点
func (this *LRUCache) MoveToTail(key int, value int) {
    node, ok := this.Mapper[key]
    if ok {
        node.Prev.Next = node.Next
	    node.Next.Prev = node.Prev
    } else {
        node = &ListNode{
			Key:   key,
			Value: value,
		}
        this.Mapper[key] = node
    }
    node.Prev = this.Tail.Prev
	node.Next = this.Tail
	this.Tail.Prev.Next = node
	this.Tail.Prev = node
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
