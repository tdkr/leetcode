/**
 * @param {ListNode} head
 * @param {number} m
 * @param {number} n
 * @return {ListNode}
 */
var reverseBetween = function(head, m, n) {
	if (head === null) return null;

	var node1 = head;
	var node2 = head;

	for (var i = 1; i < m; i++) {
		node1 = node2;
		node2 = node2.next;
	}

	var node3 = node2;
	if (node3 !== null) {
		var node4 = node3.next;
		for (var j = m; j < n; j++) {
			if (node4 === null) break;
			var tmp = node4.next;
			node4.next = node3;
			node3 = node4;
			node4 = tmp;
		}

		if (node1 !== node2) {
			node1.next = node3;
			node2.next = node4;
		} else {			
			node1.next = node4;
		}
	}

	if (m > 1) return head;

	return node3;
};