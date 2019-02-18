/**
https://leetcode.com/problems/kth-largest-element-in-a-stream/
https://en.cppreference.com/w/cpp/container/priority_queue

priority_queue 是容器适配器，它提供常数时间的（默认）最大元素查找，对数代价的插入与释出。
**/

#include <functional>
#include <queue>
#include <vector>
#include <iostream>

using namespace std;

class KthLargest
{
public:
	priority_queue<int, vector<int>, greater<int>> pq;
	int size;

	KthLargest(int k, vector<int> nums)
	{
		size = k;
		for (int i = 0; i < nums.size(); i++)
		{
			add(nums[i]);
		}
	}

	int add(int val)
	{
		if (pq.size() < size)
		{
			pq.push(val);
		}
		else if (pq.top() < val)
		{
			pq.pop();
			pq.push(val);
		}
		return pq.top();
	}
};

template <typename T>
void print_queue(T &q)
{
	while (!q.empty())
	{
		std::cout << q.top() << " ";
		q.pop();
	}
	std::cout << '\n';
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
int main()
{
	int k = 3;
	vector<int> v = {4, 5, 8, 2};
	KthLargest *kthLargest = new KthLargest(k, v);
	//	print_queue(kthLargest->pq);
	vector<int> nums = {3, 5, 10, 9, 4};
	for (int i = 0; i < nums.size(); i++)
	{
		cout << kthLargest->add(nums[i]) << endl;
	}
}
