#include <iostream> 
#include <sstream>
#include <math.h>

using namespace std;

class Solution {
public:
    int reverse(int x) {
    	int64_t result = 0;
    	while(x) {
    		int mod = x % 10;
    		x /= 10;
            result = result * 10 + mod;
		}
        return (result > INT_MAX || result < INT_MIN) ? 0 : result;
    }
};

int stringToInteger(string input) {
    return stoi(input);
}

int main() {
    string line;
    while (getline(cin, line)) {
        int x = stringToInteger(line);
        
        int ret = Solution().reverse(x);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}
