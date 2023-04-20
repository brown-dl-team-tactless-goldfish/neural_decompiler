class Solution {
private:
	void findInd(int &r, int &c, int n, int newNum) {
		r = n - 1 - ((newNum - 1) / n);
		c = (newNum - 1) % n;
		if ((n & 1) == (r & 1)) c = n - 1 - c;
	}
public:
	int snakesAndLadders(vector<vector<int>>& board) {
		queue<pair<int, int>> q;
		q.push({1, 0});
		int n = board.size();
		vector<bool> vis(n * n + 1, false);
		vis[1] = 1;
		while (q.size()) {
			int sz = q.size();
			while (sz--) {
				auto node = q.front(); q.pop();
                int num = node.first, dist = node.second;
				if (num == n * n) return dist;
				for (int i = 1; num + i <= n * n && i <= 6; ++i) {
					int r, c;
					findInd(r, c, n, num + i);
					int newNum = board[r][c]==-1?num+i:board[r][c];
					if (!vis[newNum]) {
						vis[newNum] = 1;
						q.push({newNum, dist + 1});
					}
				}
			}
		}
		return -1;
	}
};