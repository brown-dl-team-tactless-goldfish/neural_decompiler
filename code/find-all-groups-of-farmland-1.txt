class Solution {
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& a) {
        vector<vector<int>> ans;
        int n = a.size();
        int m = a[0].size();
        int offsets[] = {0, 1, 0, -1, 0};
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(a[i][j]==1)
                {
                    pair<int,int>first = {i,j};
                    pair<int,int>last = first;
                    queue<pair<int, int>> todo;
                    todo.push({i, j});
                    a[i][j]=0;
                    while (!todo.empty()) {
                        pair<int, int> p = todo.front();
                        todo.pop();
                        for (int k = 0; k < 4; k++) {
                            int r = p.first + offsets[k], c = p.second + offsets[k + 1];
                            if (r >= 0 && r < n && c >= 0 && c < m && a[r][c] == 1) {
                                a[r][c] = 0;
                                todo.push({r, c});
                                last = {r,c};
                                cout<<r<<" "<<c<<endl;
                            }
                        }
                    }
                    ans.push_back({first.first,first.second,last.first,last.second});
                }
            }
        }
        return ans;
    }
};