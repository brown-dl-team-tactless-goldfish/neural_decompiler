class Solution 
{
    public:
    class Point
    {
        public:
        int x;
        int y;

        bool operator < (Point(&P))
        {
            if (P.x == x)
                return y < P.y;
            else
                return x < P.x;
        }
        bool operator == (Point(&P))
        {
            return (x == P.x and y == P.y);
        }
};
    bool cw(Point a, Point b, Point c)
    {
        return (((b.y - a.y) * (c.x - b.x)) - ((c.y - b.y) * (b.x - a.x))) > 0;
    }
    bool acw(Point a, Point b, Point c)
    {
        return (((b.y - a.y) * (c.x - b.x)) - ((c.y - b.y) * (b.x - a.x))) < 0;
    }
    bool col(Point a, Point b, Point c)
    {
        return (((b.y - a.y) * (c.x - b.x)) - ((c.y - b.y) * (b.x - a.x))) == 0;
    }
    void convex_hull(vector<Point> &p)
    {
        if (p.size() <= 2) return;
        int n = p.size();
        sort(p.begin(), p.end());
        Point p1 = p[0], p2 = p[n - 1];
        vector <Point> up, down;
        up.push_back(p1);
        down.push_back(p1);
        for (int i = 1; i < n; i++)
        {
            if (i == n - 1 or (!acw(p1, p[i], p2)))
            {
                while (up.size() >= 2 and (acw(up[up.size() - 2], up[up.size() - 1], p[i])))
                {
                    up.pop_back();
                }
                up.push_back(p[i]);
            }
            if (i == n - 1 or (!cw(p1, p[i], p2)))
            {
                while (down.size() >= 2 and (cw(down[down.size() - 2], down[down.size() - 1], p[i])))
                {
                    down.pop_back();
                }
                down.push_back(p[i]);
            }
        }
        p.clear();
        for (int i = 0; i < up.size(); i++)
            p.push_back(up[i]);
        for (int i = 0; i < down.size(); i++)
            p.push_back(down[i]);
        sort(p.begin(), p.end());
        p.resize(unique(p.begin(), p.end()) - p.begin());
    }
    vector<vector<int>> outerTrees(vector<vector<int>>& trees) 
    {
        vector<Point> p;
        for(int i=0;i<trees.size();i++)
        {
            Point temp;      
            temp.x = trees[i][0];
            temp.y = trees[i][1];
            p.push_back(temp);
        }
        convex_hull(p);
        vector<vector<int> > ans;
        for(int i=0;i<p.size();i++)
        {
            ans.push_back({p[i].x, p[i].y});
        }
        return ans;
    }
};