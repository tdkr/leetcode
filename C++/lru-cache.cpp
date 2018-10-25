/**
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 * capacity );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
**/

#include <iostream>
#include <unordered_map>

using namespace std;


class LRUCache {
public:
	struct ListNode {
		int key, value;
        ListNode *prev,*next;
        ListNode(int k, int v)
        {
        	key = k;
        	value = v;
        	prev = NULL;
        	next = NULL;
        }		
	};	
	
    LRUCache(int cap) {
    	capacity = cap;
    	head = NULL;
    	tail = NULL;
    }
    
    int get(int key) {
    	auto it = nodeMap.find(key);
    	if(it == nodeMap.end()) {
    		return -1;
		}
		auto p = it->second;
		moveToFront(p);
		return p->value;
    }
    
    void moveToFront(ListNode *p) {
    	if(p == head) {
    		return;
		}    	
		if(p == tail) {
			p->prev->next = NULL;
			tail = p->prev; 
		}
		else {
			p->next->prev = p->prev;
			p->prev->next = p->next;
		}
    	p->next = head;
    	p->prev = NULL;
    	head->prev = p;
    	head = p;
	}
    
    void insertAtFront(ListNode *p) {
    	if(head == NULL) {
    		head = p;
    		tail = p;
    		return;
		}
    	p->next = head;
    	p->prev = NULL;
    	head->prev = p;
    	head = p;
	}
	
	void deleteFromRear() {
		if(tail == NULL) {
			return;
		}
		auto p = tail;
		nodeMap.erase(p->key);
		if(head == tail) {
			head = NULL;
			tail = NULL;
		}
		else {
			tail = tail->prev;
			tail->next = NULL;
		}
	}
    
    void put(int key, int value) {
    	auto it = nodeMap.find(key);
    	if(it == nodeMap.end()){
    		if(nodeMap.size() == capacity) {
    			deleteFromRear();
			}
    		auto p = new ListNode(key, value);
    		nodeMap[key] = p;
			insertAtFront(p);	
		}
		else {
			auto p = it->second;
			p->value = value;
			moveToFront(p);
		}
    }
    
private:
	int capacity; 
	ListNode *head, *tail;
	unordered_map<int, ListNode*> nodeMap;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
int main() {
	int capacity = 3;
	LRUCache* cache = new LRUCache( capacity );
	
	cache->put(1, 1);
	cache->put(2, 2);
	cache->put(3, 3);
	cache->put(4, 4); 
	cout << cache->get(4) << endl;     
	cout << cache->get(3) << endl;    
	cout << cache->get(2) << endl;     
	cout << cache->get(1) << endl;
	cache->put(5, 5);  
	cout << cache->get(1) << endl;	 
	cout << cache->get(2) << endl;     
	cout << cache->get(3) << endl;  
	cout << cache->get(4) << endl;   
	cout << cache->get(5) << endl;   
    return 0;
}

