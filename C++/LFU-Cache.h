#include <unordered_map>
#include <list>
#include <iterator>
using namespace std;

/**
* Your LFUCache object will be instantiated and called as such:
* LFUCache obj = new LFUCache(capacity);
* int param_1 = obj.get(key);
* obj.set(key,value);
*/
class LFUCache {
	int m_capacity = 0;
	unordered_map<int, int> m_valueMap;

	unordered_map<int, int> m_keyCountMap;
	unordered_map<int, list<int>> m_countKeyMap;
	unordered_map<int, list<int>::iterator> m_keyPosMap;

	int m_leastCount = 1;

public:
    LFUCache(int capacity) {
    	this->m_capacity = capacity;    
    }

	void updateFrequency(int key) {
		int prevCount = m_keyCountMap[key];
		m_keyCountMap[key]++;
		int curCount = m_keyCountMap[key];
		if (prevCount > 0) {
			auto it = m_keyPosMap[key];
			m_countKeyMap[prevCount].erase(it);
		}
		if (prevCount == m_leastCount && m_countKeyMap[prevCount].size() == 0) {
			m_leastCount = curCount;
		}
		if (curCount < m_leastCount) {
			m_leastCount = curCount;
		}
		auto it = m_countKeyMap[curCount].insert(m_countKeyMap[curCount].begin(), key);
		m_keyPosMap[key] = it;
	}
    
	int get(int key) {
		auto it = m_valueMap.find(key);
    	if(it != m_valueMap.end()) {
			updateFrequency(key);
			return it->second;
    	}
    	else {
    		return -1;
    	}
    }
    
    void set(int key, int value) {
		if(m_capacity == 0) {
			return;
		}

    	auto it = m_valueMap.find(key);
    	if(it != m_valueMap.end()) {
    		m_valueMap[key] = value;
    	}
    	else {
			while (m_valueMap.size() >= m_capacity) {
				int delkey = m_countKeyMap[m_leastCount].back();
				m_countKeyMap[m_leastCount].pop_back();
				m_keyCountMap[delkey] = 0;
				m_keyPosMap[delkey] = m_countKeyMap[0].end();
				m_leastCount = 1;
				it = m_valueMap.find(delkey);
				if (it != m_valueMap.end()) {
					m_valueMap.erase(it);
					break;
				}
			}
			m_valueMap[key] = value;
		}
		updateFrequency(key);
    }
};