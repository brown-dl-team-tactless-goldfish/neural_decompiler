class Graph {
    int _n = 0;
    unordered_map<int, vector<int>> _adj;
    unordered_map<int, int> _in_degree;
public:
    Graph() = default;

    explicit Graph(int n) : _n(n) {
        _adj = unordered_map<int, vector<int>>{};
        _in_degree = unordered_map<int, int>{};
        for (int i = 0; i < n; ++i) {
            _in_degree[i] = 0;
            _adj[i] = vector<int>{};
        }
    }

    explicit Graph(vector<int> &vec) {
        _n = (int) vec.size();
        _adj = unordered_map<int, vector<int>>{};
        _in_degree = unordered_map<int, int>{};
        for (const int &i : vec) {
            _in_degree[i] = 0;
            _adj[i] = vector<int>{};
        }
    }

    [[nodiscard]] int size() const {
        return _n;
    }

    [[nodiscard]] bool empty() const {
        return _n == 0;
    }

    void add_edge(int from, int to) {
        _adj[from].push_back(to);
        _in_degree[to]++;
    }

    vector<int> get_topological_order() {
        queue<int> q;
        vector<int> ans;
        unordered_map<int, int> in_degree(_in_degree);
        for (const auto &[u, degree] : in_degree) {
            if (degree == 0) 
                q.push(u);
        }

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            ans.push_back(u);
            for (const int &v : _adj[u]) {
                in_degree[v]--;
                if (in_degree[v] == 0) 
                    q.push(v);
            }
        }

        return ans;
    }
};

class Solution {
public:
    vector<int> sortItems(int n, int m, vector<int> &group, vector<vector<int>> &before_items) {
        vector<vector<int>> group_items(m);
        for (int i = 0; i < n; ++i) {
            if (group[i] >= 0) 
                group_items[group[i]].push_back(i);
            else {
                // Isolated items are put into separate groups.
                group[i] = group_items.size();
                group_items.push_back(vector<int>{i});
            }
        }

        Graph group_graph = Graph(group_items.size());
        vector<Graph> group_item_graphs(group_items.size());
        for (int i = 0; i < group_items.size(); ++i) {
            group_item_graphs[i] = Graph(group_items[i]);
        }

        for (int i = 0; i < n; ++i) {
            for (const int &item : before_items[i]) {
                int gi = group[i];
                if (gi == group[item]) // before_item is in the same group, add edge in the graph of that group.
                    group_item_graphs[gi].add_edge(item, i);
                else // before_item is in a different group, add edge in the graph of groups.
                    group_graph.add_edge(group[item], gi);
            }
        }

        vector<int> group_order = group_graph.get_topological_order();
        vector<int> ans;
        if (group_order.size() != group_graph.size()) return ans;
        for (const int &i : group_order) {
            if (group_item_graphs[i].empty())
                continue;
            vector<int> order = group_item_graphs[i].get_topological_order();
            if (order.size() != group_item_graphs[i].size()) 
                return {};
            else 
                ans.insert(ans.end(), order.begin(), order.end());
        }
        return ans;
    }
};