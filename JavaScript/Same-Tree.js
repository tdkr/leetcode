/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
	return isSameTreeIteratively(p, q);
};

var isSameTreeRecursively = function(p, q) {
	if (p === null) return q === null;
	if (q === null) return p === null;

	if (p.val === q.val) {
		return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
	} else {
		return false;
	}
}

var isSameTreeIteratively = function(p, q) {
	if (p === null) return q === null;
	if (q === null) return p === null;

	var stack = new Array(p, q);

	while (stack.length > 0) {
		var node1 = stack.shift();
		var node2 = stack.shift();

		if (node1.val !== node2.val) return false;

		if (node1.left !== null && node2.left !== null) {
			stack.push(node1.left);
			stack.push(node2.left);
		} else if (!(node1.left === null && node2.left === null)) {
			return false;
		}

		if (node1.right !== null && node2.right !== null) {
			stack.push(node1.right);
			stack.push(node2.right);
		} else if (!(node1.right === null && node2.right === null)) {
			return false;
		}
	}

	return true;
}