#include <iostream>
#include <unordered_map>
#include <list>

using namespace std;

//static const auto disable_stdio_sync = []() {
//  ios::sync_with_stdio(false);
//  cin.tie(nullptr);
//  return nullptr;
//}();

class LRUCache {
public:
    LRUCache(int capacity) : table_(capacity * 10), capacity_(capacity) {        
    }
    
    int get(int key) {
        auto it = table_.find(key);
        if (it == table_.end())
            return -1;
        queue_.splice(queue_.end(), queue_, it->second.it);
        return it->second.value;
    }
    
    void put(int key, int value) {
        queue_.push_back(key);
        auto it = table_.find(key);
        if (it != table_.end()) {
            queue_.erase(it->second.it);
            it->second.value = value;
            it->second.it = std::prev(queue_.end());
        } else {
            table_[key] = {value, std::prev(queue_.end())};
        }
        if (table_.size() > capacity_) {
            table_.erase(queue_.front());
            queue_.pop_front();
        }
    }

private:
    struct Wrapper {
        int value;
        std::list<int>::iterator it;
    };
    
    std::unordered_map<int, Wrapper> table_;
    std::list<int> queue_;
    int capacity_;
};

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
