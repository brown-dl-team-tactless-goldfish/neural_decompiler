class Solution {
private:
    vector<int> tree;

public:
    int query(int x, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) {
            return 0;
        }
        if (ql <= l && r <= qr) {
            return tree[x];
        }
        int mid = (l + r) / 2;
        return max(query(x * 2, l, mid, ql, qr), query(x * 2 + 1, mid + 1, r, ql, qr));
    }

    void update(int x, int l, int r, int u, int value) {
        if (l > u || r < u) {
            return;
        }
        if (l == r) {
            tree[x] = value;
            return;
        }
        int mid = (l + r) / 2;
        update(x * 2, l, mid, u, value);
        update(x * 2 + 1, mid + 1, r, u, value);
        tree[x] = max(tree[x * 2], tree[x * 2 + 1]);
    }

    int maxJumps(vector<int>& arr, int d) {
        int n = arr.size();
        vector<int> bound_l(n), bound_r(n);

        stack<int> s;
        for (int i = 0; i < n; ++i) {
            while (!s.empty() && arr[s.top()] <= arr[i]) {
                bound_r[s.top()] = min(i - 1, s.top() + d);
                s.pop();
            }
            s.push(i);
        }
        while (!s.empty()) {
            bound_r[s.top()] = min(n - 1, s.top() + d);
            s.pop();
        }

        for (int i = n - 1; i >= 0; --i) {
            while (!s.empty() && arr[s.top()] <= arr[i]) {
                bound_l[s.top()] = max(i + 1, s.top() - d);
                s.pop();
            }
            s.push(i);
        }
        while (!s.empty()) {
            bound_l[s.top()] = max(0, s.top() - d);
            s.pop();
        }

        vector<int> order(n);
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int i, int j) {return arr[i] < arr[j];});

        vector<int> f(n);
        tree.resize(n * 4 + 10);
        for (int id: order) {
            int prev = 0;
            if (bound_l[id] < id) {
                prev = max(prev, query(1, 0, n - 1, bound_l[id], id - 1));
            }
            if (id < bound_r[id]) {
                prev = max(prev, query(1, 0, n - 1, id + 1, bound_r[id]));
            }
            f[id] = prev + 1;
            update(1, 0, n - 1, id, f[id]);
        }

        return *max_element(f.begin(), f.end());
    }
};