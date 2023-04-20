class Solution {
public:
    int mn = 10000;
    int mx = 0;
    int first;
    int second;
    void dfs(vector<int> &arr, int round) {
        int size = arr.size() / 2;
        if(arr.size() == 1) return;
        for(int i = 0; i < size; i++) {
            //if we can match first and second in this round.
            if(arr[i] == first && arr[arr.size() - i - 1] == second) {
                mn = min(mn, round);
                mx = max(mx, round);
                return;
            }
        }
        bool f1 = false, f2 = false;
        for(auto n : arr) {
            f1 |= n == first;
            f2 |= n == second;
        }
        if(!f1 || !f2) { //can not find first and second player.
            return;
        }
        vector<int> nextarr(size + (arr.size() % 2));
        int m = (1 << size) - 1;
        for(int i = 0; i <= m; i++) { //try all the winning status for the left side players.
            int left = 0, right = nextarr.size() - 1;
            for(int j = 0; j < size; j++) {
                if((1 << j) & i) { //left side player win, put it to the next array.
                    nextarr[left++] = arr[j];
                }else { //right side player win.
                    nextarr[right--] = arr[arr.size() - j - 1];
                }
                
            }
            if(arr.size() % 2) { //middle player go to the next round.
                nextarr[left] = arr[arr.size() / 2];
            }
            dfs(nextarr, round + 1);
        }
    }
    vector<int> earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        vector<int> arr(n);
        for(int i= 1; i <= n; i++) {
            arr[i - 1] = i;
        }
        first = firstPlayer;
        second = secondPlayer;
        dfs(arr, 1);
        return {mn, mx};
    }
};