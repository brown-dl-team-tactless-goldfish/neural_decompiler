class Solution {
public:
    vector<int> movesToStamp(string stamp, string target) {
       vector<int> res;
        bool matched = true;
        while (matched) {  
            matched = false;
            for (int i = 0; i <= target.size() - stamp.size(); ++i) { 
                int j = 0, stars_cnt = 0;
				//find a match with stamp.
                for (; j < stamp.size(); ++j) {
                    
                    if (target[i + j] == '*') {
                        ++stars_cnt;
                    } else if (target[i + j] != stamp[j]) {
                        break;
                    }
                }  
			//let if we find a match with stamp, do a reverse operation on target.
                if (j == stamp.size() && stars_cnt < stamp.size()) {
                    res.push_back(i);
                    
                    for (int k = 0; k < stamp.size(); ++k) {
                        target[i + k] = '*';
                    }
                    matched = true;
                }
            }
        }
        for (auto c : target) {
            if (c != '*') {
                return vector<int>();
            }
        }
        reverse(res.begin(), res.end());
        return res;  
    }
};