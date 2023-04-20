class Solution
{
public:
    bool isBoomerang(vector<vector<int>> &points)
    {
        vector<int> a;
        vector<int> b;
        vector<int> c;
        a = points[0];
        b = points[1];
        c = points[2];
        return ((a[0] - b[0]) * (b[1] - c[1])) != ((b[0] - c[0]) * (a[1] - b[1]));
    }
};