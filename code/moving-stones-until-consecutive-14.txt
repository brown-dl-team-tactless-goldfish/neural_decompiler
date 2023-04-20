class Solution {
public:
    vector<int> numMovesStones(int a, int b, int c) {
        vector< int> v{a,b,c};
        vector< int> res;
        sort(v.begin(), v.end());
        a = v[0];
        b = v[1];
        c = v[2];

        int ans = (b-a-1) + (c-b-1);

        res.push_back(ans);
        ans = 0;

        if(a+1!=b) ans++;
        if(b+1!=c) ans++;
        if(b-a == 2 || c-b == 2) ans = 1; 
        res.push_back(ans);
        reverse(res.begin(),res.end());
        return res;
    }
};