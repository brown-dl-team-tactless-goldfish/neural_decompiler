class Solution {
public:
    // Returns a range that pivot can be possibly at after reversing a subarray with length k.
    inline pair<int, int> getRange(int n, int pivot, int k) {
		// Left most subarray containing pivot
        int l1 = max(0, pivot - k + 1);
        int r1 = l1 + k - 1;
		
		// Right most subarray containing pivot
        int r2 = min(n - 1, pivot + k - 1);
        int l2 = r2 - k + 1;
		
		int left = r1 - (pivot - l1);
        int right = l2 + (r2 - pivot);
        return {left, right};
    }
    
    vector<int> minReverseOperations(int n, int p, vector<int>& banned, int k) {
        unordered_set<int> bans(banned.begin(), banned.end());
        vector<int> ans(n, -1);
        // BST to store all nodes not visited yet.
        set<int> s[2];

        ans[p] = 0;
        // Put all available postions in BST, split by parity
        for (int i = 0; i < n; i ++)
            if (i != p && bans.find(i) == bans.end())
                s[i & 1].insert(i);
        
        // Queue for BFS floodfill.
        queue<int> q;
        q.push(p);
        while (!q.empty()) {
            int pivot = q.front();
            q.pop();
            auto range = getRange(n, pivot, k);

            // for current pivot, check if it will visit even positions or odd positions. 
            int o = (k % 2 == 0) ? (1 - pivot & 1) : (pivot & 1);
            //int o = (k & 1) ^ (pivot & 1) ^ 1;

            // Find all reachable indexes range on the tree.
            auto bg = s[o].lower_bound(range.first);
            auto ed = s[o].upper_bound(range.second);

            // Visit reachable indexes and update answer.
            for (auto it = bg; it != ed; it ++) {
                ans[*it] = ans[pivot] + 1;
                q.push(*it);
            }

            // Remove visited indexes from tree.
            s[o].erase(bg, ed);
        }

        return ans;
    }
};