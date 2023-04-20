class Solution {
public:
    bool isvalid(int i, int j, int n, int m){
        return i>=0 && i<n && j>=0 && j<m;
    }
    int minDays(vector<vector<int>>& grid) {
        vector<pair<int, int>>po;
        vector<vector<int>>v(grid.size(), vector<int>(grid[0].size(), 0));
        int cnt=0;
        for(int i=0; i<v.size(); i++){
            for(int j=0; j<v[0].size(); j++){
                if(!v[i][j] && grid[i][j]){
                    po.push_back({i, j});
                    cnt++;
                    v[i][j]=1;
                    queue<pair<int, int>>q;
                    q.push({i, j});
                    while(!q.empty()){
                        int x=q.front().first, y=q.front().second;
                        q.pop();
                        int c[4]={0, -1, 0, 1};
                        int r[4]={-1, 0, 1, 0};
                        for(int k=0; k<4; k++){
                            int row=r[k]+x, col=c[k]+y;
                            if(isvalid(row, col, grid.size(), grid[0].size())){
                                if(!v[row][col] && grid[row][col]){
                                    po.push_back({row, col});
                                    v[row][col]=1;
                                    q.push({row, col});
                                }
                            }
                        }
                    }
                }
            }
        }
        if(cnt==0 || cnt>1){return 0;}
        else{
            for(int i=0; i<po.size(); i++){
                v[po[i].first][po[i].second]=0;
                vector<vector<int>>chk(v.size(), vector<int>(v[0].size(), 0));
                int cnt1=0;
                for(int x=0; x<v.size(); x++){
                    for(int j=0; j<v[0].size(); j++){
                        if(v[x][j] && !chk[x][j]){
                            cnt1++;
                            //cout<<x<<" "<<j<<endl;
                            chk[x][j]=1;
                            queue<pair<int, int>>q;
                            q.push({x, j});
                            while(!q.empty()){
                                int x=q.front().first, y=q.front().second;
                                q.pop();
                                int c[4]={0, -1, 0, 1};
                                int r[4]={-1, 0, 1, 0};
                                for(int k=0; k<4; k++){
                                    int row=r[k]+x, col=c[k]+y;
                                    if(isvalid(row, col, grid.size(), grid[0].size())){
                                        if(!chk[row][col] && v[row][col]){
                                            chk[row][col]=1;
                                            q.push({row, col});
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                //cout<<cnt1<<endl;
                if(cnt1>1 || cnt1==0){return 1;}
                else{v[po[i].first][po[i].second]=1;}
            }
        }
        return 2;
    }
};