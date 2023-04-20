class Solution {
public:
vector<int> decode(vector<int>& encoded) {

    int n = encoded.size();

    int temp = 0;
    for (int i = 0; i < n ; i += 2) {
        temp = temp ^ encoded[i];
    }
    for (int i = 1; i <= n + 1; i++) {
        temp = temp ^ i;
    }

    vector<int> ans;
    ans.push_back(temp);

    int j = n - 1;
    while (j >= 0) {
        ans.push_back(ans[ans.size() - 1] ^ encoded[j--]);
    }

    reverse(ans.begin(), ans.end());
    return ans;
}
};