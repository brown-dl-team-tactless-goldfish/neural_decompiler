class Solution {
public:
	int n;

	vector<int> bfs(int node,vector<pair<int,int>>adj[]){
	priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>q;
	vector<int>distance(n,INT_MAX);
	distance[node]=0;
	q.push({0,node});

	while(!q.empty()){
		int dist= q.top().first;
		int prev = q.top().second;
		q.pop();
		for(auto x: adj[prev]){
			int next = x.first;
			int nextDistance = x.second;
			if(distance[next]>dist+nextDistance){
				distance[next] = dist+nextDistance;
				q.push({distance[next],next});
			}
		}
	}
	return distance; 
}

	int closestMeetingNode(vector<int>& edges, int node1, int node2) {
		n = edges.size();
		vector<pair<int,int>>adj[n];
		for(int i=0;i<n;i++) if(edges[i]>=0) adj[i].push_back({edges[i],1});
		vector<int>dis1 = bfs(node1,adj);
		vector<int>dis2 = bfs(node2,adj);
		int res = -1,maxi = INT_MAX;
		for(int i=0;i<n;i++){
		  if(dis1[i]!=INT_MAX and dis2[i]!=INT_MAX){
			  if(maxi>max(dis1[i],dis2[i])) {
				  maxi = max(dis1[i],dis2[i]);
				  res = i;
			  }
		  }  
		}
		return res;
	}
};