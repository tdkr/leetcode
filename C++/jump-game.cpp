#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
	bool canReachEnd(vector<int>& nums, vector<int>& mark, int index) {
		if(index == nums.size() - 1) {
			return true;
		}
		if(mark[index] == -1) {
			int value = nums[index];
			for(int i = 1; i <= value; i++) {
				if(canReachEnd(nums, mark, index+i)) {
					mark[index] = 1;
					return true;
				}		
			}
		} 		
		mark[index] = 0;
		return false;
	}
	
    bool canJump(vector<int>& nums) {
    	int endIndex = nums.size() - 1;
        vector<int> mark(nums.size(), -1);
        return canReachEnd(nums, mark, 0);
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

string boolToString(bool input) {
	return input ? "True" : "False";
}

int main() {
    string line;
    while (getline(cin, line)) {
        vector<int> nums = stringToIntegerVector(line);
        
        bool ret = Solution().canJump(nums);

        string out = boolToString(ret);
        cout << out << endl;
    }
    return 0;
}
