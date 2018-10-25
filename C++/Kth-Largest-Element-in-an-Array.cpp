/**
Kth Largest Element in an Array
**/
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>

using namespace std;

class Solution {
public:
	priority_queue<int, vector<int>, greater<int>> pq;
	int size;
	
    int findKthLargest(vector<int>& nums, int k) {
        size = k;
    	for(int i=0; i<nums.size();i++) {
    		add(nums[i]);
		}    	
		return pq.top();
    }
    
    void add(int val) {    	
		if(pq.size() < size) {
			pq.push(val);
		} else if(pq.top() < val) {
			pq.pop();
			pq.push(val);
		} 
	} 
};

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}

vector<int> stringToIntegerVector(string input) {
    vector<int> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) {
        output.push_back(stoi(item));
    }
    return output;
}

int stringToInteger(string input) {
    return stoi(input);
}

int main() {
    string line;
    while (getline(cin, line)) {
        vector<int> nums = stringToIntegerVector(line);
        getline(cin, line);
        int k = stringToInteger(line);
        
        int ret = Solution().findKthLargest(nums, k);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}
