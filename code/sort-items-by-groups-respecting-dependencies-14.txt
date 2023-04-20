class Solution {
public:
	vector<vector<int>> graph;
	vector<int> visited;
	vector<int> done;
	vector<int> visited_gr;
	vector<int> done_gr;
	vector<int> group;
	vector<vector<int>> beforeItems;
	vector<int> ans;

	bool sort_group(int gr)
	{
		if (visited_gr[gr]) 
			return done_gr[gr];
		visited_gr[gr] = true;

		for (auto item : graph[gr]) {
			for (auto child : beforeItems[item]) {
				if (group[child] == -1 && !add(child))
					return false;

				if (group[child] != -1 && group[child] != gr && !sort_group(group[child]))
					return false;
			}
		}

		for (auto item : graph[gr]) {
			if (!dfs(item, gr))
				return false;
		}

		done_gr[gr] = true;
		return true;
	}

	bool add(int item) { // push item have no group or group[item] = -1
		if (visited[item])
			return done[item];
		visited[item] = true;

		for (auto child : beforeItems[item]) {
			if (group[child] == -1 && !add(child))
				return false;

			if (group[child] != -1 && !sort_group(group[child]))
				return false;
		}
		done[item] = true;
		ans.push_back(item);
		return true;
	}

	bool dfs(int item, int gr) {
		if (visited[item])
			return done[item];
		visited[item] = true;

		for (auto child : beforeItems[item]) {
			if (group[child] != gr)
				continue;

			if (!dfs(child, gr))
				return false;
		}
		done[item] = true;
		ans.push_back(item);
		return true;
	}

	vector<int> sortItems(int n, int m, vector<int> &g, vector<vector<int>> &b) {
		graph.resize(m);
		visited.resize(n);
		done.resize(n);
		visited_gr.resize(m);
		done_gr.resize(m);
		group = g;
		beforeItems = b;
		for (int i = 0; i < n; i++) {
			if (group[i] != -1)
				graph[group[i]].push_back(i);
		}

		for (int i = 0; i < n; i++) {
			if (group[i] == -1 && !add(i))
				return {};
			if (group[i] != -1 && !sort_group(group[i]))
				return {};
		}

		return ans;
	}
};