class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& v) {
      vector<int> cnt(10,0), ans;
	for (int d: v) cnt[d]++;  

	for (int i=1; i<10; i++) {
		if (cnt[i]==0) continue;
		cnt[i]--;
		for (int j=0; j<10; j++) {
			if (cnt[j]==0) continue;
			cnt[j]--;
			for (int k=0; k<10; k+=2) {
				if (cnt[k]==0) continue;
				ans.push_back(100*i+10*j+k);
			}
			cnt[j]++; // backtrack
		}
		cnt[i]++;     // backtrack
	}
	return ans;        
    }
};