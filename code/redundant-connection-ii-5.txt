class DSU
{
	public:
	vector<int> arr;
	DSU(int n)
	{
		arr.assign(n+1,0);
		for(int i=1;i<=n;i++)
		{
			arr[i]=i;
		}
	}

	int find(int a)
	{
		if(arr[a]!=a)
		{
			arr[a]=find(arr[a]);
		}

		return arr[a];
	}

	void merge(int a, int b)
	{
		int x=find(a);
		int y=find(b);
		arr[x]=arr[y];
	}


};
class Solution {
public:
	vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
		int n=edges.size();
		vector<int> parent(n+1);

		vector<int> ans1;
		vector<int> ans2;
		for(auto& x:edges)
		{
			if(parent[x[1]]>0)
			{
				ans1.push_back(parent[x[1]]);
				ans1.push_back(x[1]);

				ans2=x;

				x[0]=-1;
				x[1]=-1;

			}
			else
			{
				parent[x[1]]=x[0];
			}


		   //cout<<x[1]<<" "<<x[0]<<endl;
		}

		DSU* dsu=new DSU(n);


		for(auto& x:edges)
		{
			if(x[0]<0 || x[1]<0) continue;
			if(dsu->find(x[0])==dsu->find(x[1]))
			{
				if(ans2.empty()) return x;
				else return ans1;
			}
			dsu->merge(x[0],x[1]);
		}

		return ans2;




	}
};