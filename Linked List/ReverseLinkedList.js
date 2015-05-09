/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
	return reverseListIteratively(head);
};

var reverseListRecursively = function(head) {
	if (head === null) return null;

	if (head.next !== null) {
		var tail = reverseList(head.next);
		head.next.next = head;
		head.next = null;
		return tail;
	}
	else
	{
		return head;
	}
};

var reverseListIteratively = function(head) {
	if (head === null) return null;

	var node1 = head;
	var node2 = head.next;
	while(node2 !== null)
	{
		var tmpNode = node2.next;
		node2.next = node1;
		node1 = node2;
		node2 = tmpNode;
	}

	head.next = null;

	return node1;
};