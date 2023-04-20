class Solution {
public:
	bool checkValid(vector<vector<int>>& matrix) {
		int n = matrix.size();
		if(n == 1){
			return  true;
		}
		unordered_map<int, int> m;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if(m.count(matrix[i][j])){
					return false;
				}
				else{
					m[matrix[i][j]]++;
				}
			}
			m.clear();
		}
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if(m.count(matrix[j][i])){
					return false;
				}
				else{
					m[matrix[j][i]]++;
				}
			}
			m.clear();
		}
		return true;
	}
};