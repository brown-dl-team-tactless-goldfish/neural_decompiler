class Solution {
public:
    int shoppingOffers(const vector<int>& price, const vector<vector<int>>& special, const vector<int>& needs) {
        int result = inner_product(price.begin(), price.end(), needs.begin(), 0);
        for (const vector<int>& offer : special) {
            vector<int> r = can(needs, offer);
            if (r.empty()) continue;
            result = min(result, offer.back() + shoppingOffers(price, special, r));
        }
        return result;
    }
    vector<int> can(const vector<int>& needs, const vector<int>& offer) {
        vector<int> r(needs.size(), 0);
        for (int i = 0, n = needs.size(); i < n; ++i) {
            if (offer[i] > needs[i]) return vector<int>();
            r[i] = needs[i] - offer[i];
        }
        return r;
    }
};