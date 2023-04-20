class findunion {
 public:
      findunion(int n) : id(n), rank(n) {
    iota(begin(id), end(id), 0);
  }

  void operationonrank(int u, int v) {
    const int i = find(u);
    const int j = find(v);
    if (i == j)
      return;
    if (rank[i] < rank[j]) {
      id[i] = id[j];
    } else if (rank[i] > rank[j]) {
      id[j] = id[i];
    } else {
      id[i] = id[j];
      ++rank[j];
    }
  }

  int find(int u) {
    return id[u] == u ? u : id[u] = find(id[u]);
  }

 private:
  vector<int> id;
  vector<int> rank;
};

class Solution {
 public:
  int numberOfGoodPaths(vector<int>& vals, vector<vector<int>>& edges) {
    const int n = vals.size();
    int ans = n;
    findunion uf(n);
    vector<vector<int>> Graph(n);
    map<int, vector<int>> nodevalue;

    for (int i = 0; i < vals.size(); ++i)
      nodevalue[vals[i]].push_back(i);

    for (const vector<int>& edge : edges) {
      const int u = edge[0];
      const int v = edge[1];
      if (vals[v] <= vals[u])
        Graph[u].push_back(v);
      if (vals[u] <= vals[v])
        Graph[v].push_back(u);
    }

    for (const auto& [val, nodes] : nodevalue) {
      for (const int u : nodes)
        for (const int v : Graph[u])
          uf.operationonrank(u, v);
      unordered_map<int, int> count_of_root;
      for (const int u : nodes)
        ++count_of_root[uf.find(u)];
      for (const auto& [_, count] : count_of_root)
        ans += count * (count - 1) / 2;
    }

    return ans;
    }
};