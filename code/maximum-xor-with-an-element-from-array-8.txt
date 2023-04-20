class Node {
private:
    Node* links[2];
public:
    bool contains(int bit) {
        return (links[bit] != NULL);
    }
    void put(int bit, Node* node) {
        links[bit] = node;
    }
    Node* get(int bit) {
        return links[bit];
    }
};

class Trie {
private:
    Node* root;
public:
    Trie() {
        root = new Node();
    }
    void insert(int num) {
        Node* node = root;
        for (int i = 31; i >= 0; --i) {
            int bit = (num >> i) & 1;
            if (!node->contains(bit)) {
                node->put(bit, new Node());
            }
            node = node->get(bit);
        }
    }
    int maxXor(int num) {
        Node* node = root;
        int mx = 0;
        for (int i = 31; i >= 0; --i) {
            int bit = (num >> i) & 1;
            if (node->contains(1-bit)) {
                mx = mx | (1 << i);
                node = node->get(1-bit);
            } else {
                node = node->get(bit);
            }
        }
        return mx;
    }
};

class Solution {
public:
    vector<int> maximizeXor(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), m = queries.size();
        Trie trie;
        vector<int> result(m, 0);
        sort(nums.begin(), nums.end());
        for (int i = 0; i < queries.size(); i++) {
            queries[i].push_back(i);
        }
        sort(queries.begin(), queries.end(), [](vector<int> &lhs, vector<int> &rhs) {
            return lhs[1] < rhs[1];
        });
        int i = 0;
        for (auto query : queries) {
            int x = query[0], a = query[1], ind = query[2];
            while (i < n && nums[i] <= a) {
                trie.insert(nums[i]);
                i++;
            }
            if (i == 0) result[ind] = -1;
            else result[ind] = trie.maxXor(x);
        }
        return result;
    }
};