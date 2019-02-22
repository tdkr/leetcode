/**longest-substring-without-repeating-characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
**/

#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>
#include <assert.h>
#include <algorithm>

using namespace std;


class Solution {
public:		
    int lengthOfLongestSubstring(string s) {
//    	printf("lengthOfLongestSubstring, %s\n", s.c_str());
    	unordered_map<char, int> charMap;
    	int maxLen = 0, start = -1;
		for(int i = 0; i < s.length(); i++) {
			char c = s[i];
			auto it = charMap.find(c);
			if(it != charMap.end() && it->second > start) {
				start = it->second;
			}
			charMap[c] = i;
//			printf("%d, %d, %d\n", maxLen, i, start);
			maxLen = max(maxLen, i - start);
		}
		return maxLen;
    }
    
   
//   int lengthOfLongestSubstring(string s) {
//        vector<int> dict(256, -1);
//        int maxLen = 0, start = -1;
//        for (int i = 0; i != s.length(); i++) {
//            if (dict[s[i]] > start)
//                start = dict[s[i]];
//            dict[s[i]] = i;
//            maxLen = max(maxLen, i - start);
//        }
//        return maxLen;
//    }
};

string stringToString(string input) {
    assert(input.length() >= 2);
    string result;
    for (int i = 1; i < input.length() -1; i++) {
        char currentChar = input[i];
        if (input[i] == '\\') {
            char nextChar = input[i+1];
            switch (nextChar) {
                case '\"': result.push_back('\"'); break;
                case '/' : result.push_back('/'); break;
                case '\\': result.push_back('\\'); break;
                case 'b' : result.push_back('\b'); break;
                case 'f' : result.push_back('\f'); break;
                case 'r' : result.push_back('\r'); break;
                case 'n' : result.push_back('\n'); break;
                case 't' : result.push_back('\t'); break;
                default: break;
            }
            i++;
        } else {
          result.push_back(currentChar);
        }
    }
    return result;
}

int main() {
    string line;
    while (getline(cin, line)) {
        string s = stringToString(line);
        
        int ret = Solution().lengthOfLongestSubstring(s);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}
