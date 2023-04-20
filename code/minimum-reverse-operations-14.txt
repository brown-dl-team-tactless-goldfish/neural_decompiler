class Solution {
public:
    vector<int> minReverseOperations(int n, int p, vector<int>& banned, int k) {
        // create a boolean array to check if index i is banned in linear time
        vector<bool> isBanned(n, false);
         for (auto &i : banned)
            isBanned[i] = true;

        // create return array, which will be the return value
        vector<int> ret(n, -1);
        // because arr[p] is 1 without any operation, ret[p] is assigned 0        
        ret[p] = 0;

        if (k == 1) // in this case, arr remains invariant after every operation
            return ret;


        // create two sets, for odd and even indices respectively
        set<int> odd, even;
        for (int i = 0 ; i < n ; ++i) {
            if (!isBanned[i]) {
                if (i % 2) {
                    odd.insert(i);
                }
                else {
                    even.insert(i);
                }
            }
        }
        
        queue<pair<int,int> > statuses; // (idx, ops)

        // initial status
        statuses.push(make_pair(p, 0));
        if (p % 2)
            odd.erase(odd.find(p));
        else
            even.erase(even.find(p));

        while (!statuses.empty()) {
            auto tmp = statuses.front();
            statuses.pop();
            
            int i = tmp.first, ops = tmp.second;
            
            // the smallest and biggest possible index after 1 operation
            int smallest = 2 * max(0, i - k + 1) + k - 1 - i, biggest = 2 * min(n - k, i) + k - 1 - i;

            // determine the parity of possible indices after 1 operation
            if (smallest % 2) { // find in odd

                for (auto it = odd.lower_bound(smallest) ; it != odd.end() && *it <= biggest ;) {
                    statuses.push(make_pair(*it, ops + 1));
                    ret[*it] = ops + 1;
                    odd.erase(it++);
                }

            }
            else { // find in even

                for (auto it = even.lower_bound(smallest) ; it != even.end() && *it <= biggest ;) {
                    statuses.push(make_pair(*it, ops + 1));
                    ret[*it] = ops + 1;
                    even.erase(it++);
                }
            }
            
        }
        
        return ret;
    }
};