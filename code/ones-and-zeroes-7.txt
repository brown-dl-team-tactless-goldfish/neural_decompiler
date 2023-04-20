class Solution {
public:
	pair<int, int> count01(string& str) { // first is the number of '0' in str, second is the number of '1' in str
		pair<int, int> ans;
		for(auto& c : str) {
			ans.first += (c == '0');
			ans.second += (c == '1');
		}
		return ans;
	}

	int findMaxForm(vector<string>& strs, int m, int n) {        
		vector<vector<int>> maxSizeSubset(m + 1, vector<int>(n + 1)); //maxSizeSubset[i][j] is max size of subset contains max i charactor '0' and j charactor '1'

		for(auto& str : strs) {
			auto [count0, count1] = count01(str);

			for(int size0 = m; size0 >= 0; size0--) {
				for(int size1 = n; size1 >= 0; size1--) {
					if(size0 < count0 || size1 < count1)
						continue;
					maxSizeSubset[size0][size1] = max(maxSizeSubset[size0][size1], 
													  maxSizeSubset[size0 - count0][size1 - count1] + 1);
				}
			}
		}

		return maxSizeSubset[m][n];
	}
};