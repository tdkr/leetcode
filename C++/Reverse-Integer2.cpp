#include <iostream>
#include <sstream>
#include <math.h>

using namespace std;

class Solution
{
  public:
    int reverse(int x)
    {
        int result = 0;
        while (x != 0)
        {
            int mod = x % 10;
            x /= 10;
            int tmp = result;
            result = result * 10 + mod;
            if (result / 10 != tmp) {
                return 0;
            }
        }
        return result;
    }
};

int stringToInteger(string input)
{
    return stoi(input);
}

int main()
{
    string line;
    while (getline(cin, line))
    {
        int x = stringToInteger(line);

        int ret = Solution().reverse(x);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}
