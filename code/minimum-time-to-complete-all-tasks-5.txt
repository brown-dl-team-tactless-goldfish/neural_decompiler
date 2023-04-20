class Solution {
public:
    int findMinimumTime(vector<vector<int>>& tasks) {
        sort(tasks.begin(), tasks.end(), [](const vector<int>& a, const vector<int>& b){return a[1] < b[1];});
        int ans = 0;
        int work [2001] = {};
        for(auto & i : tasks){
            for(int j = i[0]; j <= i[1]; j++) i[2] -= work[j];
            if(i[2] > 0){
                ans += i[2];
                for(int j = i[1]; j >= 0 && i[2]>0; j--){
                    if(work[j] == 0) {
                        work[j]++;
                        i[2]--;
                    }
                }
            }
        }
        return ans;
    }
};