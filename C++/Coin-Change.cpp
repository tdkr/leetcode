/**Coin Change
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1, 4, 5], amount = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4
Example 2:

Note:
You may assume that you have an infinite number of each kind of coin.
**/

#include <iostream> 
#include <sstream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;
 
class Solution {
public:	
    int coinChange(vector<int>& coins, int amount) {
    	int max = amount+1;
    	vector<int> dp(amount+1, max);    
		dp[0] = 0;	
		
		for(int c : coins) {
			for(int i = c; i <= amount; i++) {
				dp[i] = min(dp[i], dp[i-c]+1);
			}
		}
		
//    	for(int i = 1; i <= amount; i++) {
//			for(int j = 0; j < coins.size(); j++) {
//				if (dp[i] > 1 && coins[j] <= i) {
//					printf("%d : %d, %d\n", i, dp[i], dp[i-coins[j]]+1);
//					dp[i] = min(dp[i], dp[i-coins[j]]+1);
//				}
//			}    			
//		}

		int ret = dp[amount] == max ? -1 : dp[amount];
		return ret;
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
        vector<int> coins = stringToIntegerVector(line);
        getline(cin, line);
        int amount = stringToInteger(line);
        
        int ret = Solution().coinChange(coins, amount);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}
