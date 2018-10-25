/*
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
*/

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <list>

using namespace std;

class Solution {
public:	
    string largestNumber(vector<int>& nums) {
    	vector<string> arr;
        for(int i : nums) {
        	arr.push_back(to_string(i));
		}
		sort(arr.begin(), arr.end(), compare);
		string ret;
		for(string s:arr) {
			cout << s << ","; 
			ret += s;
		}
		if(ret[0] == '0' && ret.size() > 1) {
			return "0";
		}
		return ret;
    }
    
private:
	static bool compare(const string& s1, const string& s2) {
		return s1 + s2 > s2 + s1;
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

int main() {
    string line;
    while (getline(cin, line)) {
        vector<int> nums = stringToIntegerVector(line);
        
        string ret = Solution().largestNumber(nums);

        string out = (ret);
        cout << out << endl;
    }
    return 0;
}
