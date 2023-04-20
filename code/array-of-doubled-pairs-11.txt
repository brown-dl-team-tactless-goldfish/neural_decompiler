class Solution {
public:
    bool canReorderDoubled(vector<int>& arr) {
        unordered_map<int, int> m;
        int z = 0, cnt = 0;
        for(int  i : arr) {
            if(!i) z++;
            else m[i]++;
        }
        if(z % 2) return false;
        cnt += z / 2;
        
        sort(arr.begin(), arr.end());
        for(int i : arr) {
            if(m.find(i) == m.end()) continue;
            if(m.find(2 * i) != m.end()) {
                m[2 * i]--, m[i]--;
                if(!m[2 * i]) m.erase(2 * i);
                if(!m[i]) m.erase(i);
                cnt++;
            }
        }
        return cnt == arr.size() / 2;
    }
};