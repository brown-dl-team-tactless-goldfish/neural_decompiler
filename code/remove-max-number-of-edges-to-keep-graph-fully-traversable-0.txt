class Solution {
    vector<int> alice, bob;
    static bool comp(vector<int> &a, vector<int> &b)
    {
        return a[0] > b[0];
    }
    int find_alice(int v)
    {
        if(v == alice[v])
            return v;
        return alice[v] = find_alice(alice[v]);
    }
    int find_bob(int v)
    {
        if(v == bob[v])
            return v;
        return bob[v] = find_bob(bob[v]);
    }
    void union_alice(int a, int b)
    {
        a = find_alice(a);
        b = find_alice(b);
        if(a == b)
            return;
        alice[b] = a;
        return;
    }
    void union_bob(int a, int b)
    {
        a = find_bob(a);
        b = find_bob(b);
        if(a == b)
            return;
        bob[b] = a;
        return;
    }
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        sort(edges.begin(), edges.end(), comp);
        for(int i = 0; i <= n; i++)
        {
            alice.push_back(i);
            bob.push_back(i);
        }
        int ans = 0;
        for(vector<int> &v : edges)
        {
            if(v[0] == 3)
            {
                int xa = find_alice(v[1]);
                int ya = find_alice(v[2]);
                int xb = find_bob(v[1]);
                int yb = find_bob(v[2]);
                if(xa == ya && xb == yb)
                {
                    ans++;
                }
                else
                {
                    if(xa != ya)
                        union_alice(xa, ya);
                    if(xb != yb)
                        union_bob(xb, yb);
                }
            }
            else if(v[0] == 2)
            {
                int xb = find_bob(v[1]);
                int yb = find_bob(v[2]);
                if(xb == yb)
                    ans++;
                else
                {
                    union_bob(xb, yb);
                }
            }
            else
            {
                int xa = find_alice(v[1]);
                int ya = find_alice(v[2]);
                if(xa == ya)
                    ans++;
                else
                    union_alice(xa, ya);
            }
        }
        int vala, valb;
        for(int i = 1; i <= n; i++)
        {
            if(i == 1)
            {
                vala = find_alice(i);
                valb = find_bob(i);
            }
            else
            {
                if(vala != find_alice(i))
                {
                    return -1;
                }
                if(valb != find_bob(i))
                {
                    return -1;
                }
            }
        }
        return ans;
    }
};