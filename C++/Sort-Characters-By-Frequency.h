#include <string>
#include <unordered_map>
#include <vector>
#include <iostream>
#include <ctime>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace std::chrono;

class Solution {

public:
    string frequencySort(string s) {
		unordered_map<char, int> freq;
		vector<string> bucket(s.size() + 1, "");
		string res;

		for (char c : s) {
			freq[c]++;
		}

		for (auto& it : freq) {
			int n = it.second;
			char c = it.first;
			bucket[n].append(n, c);
		}

		//form descending sorted string
		for (int i = s.size(); i>0; i--) {
			if (!bucket[i].empty())
				res.append(bucket[i]);
		}

		return res;
	}

	string frequencySort2(string s) {
		unordered_map<char, int> freq;

		for (char c : s) {
			freq[c]++;
		}

		std::sort(s.begin(), s.end(), [&](const char x, const char y) -> bool {
			int n1 = freq[x];
			int n2 = freq[y];
			return n1 == n2 ? x > y : n1 > n2;
		});

		return s;
	}
};