class Solution
{
public:
    int minimumOperations(vector<int> &nums)
    {
        if (nums.size() == 1)
            return 0;
        int cnt = 0;
        map<int, int> m, g;
        
        //storing count of value of indices at odd and even position
        for (int i = 0; i < nums.size(); i += 2)
        {
            m[nums[i]]++;
        }
        for (int i = 1; i < nums.size(); i += 2)
            g[nums[i]]++;
        
        
        vector<pair<int, int>> a, b;
        
        int zeropos = 0, zeroposval = 0;

        //Pushing value into the pair of vector as p.first is count of occ and p.second is value 
        for (auto c : m)
        {
            a.push_back({c.second, c.first});
        }
        for (auto c : g)
            b.push_back({c.second, c.first});
        
        int firstpos = 0, firstposval = 0;
        
        //sort the vector pair array in desc order
        sort(a.begin(), a.end(),greater<pair<int,int>>());
        sort(b.begin(), b.end(),greater<pair<int,int>>());

        firstpos = b[0].first;
        zeropos = a[0].first;
        firstposval = b[0].second;
        zeroposval = a[0].second;

        int i = 0, j = 0;
        while (i < a.size() and j < b.size())
        {
            if (a[i].second == b[j].second)
            {
                if (a[i].first > b[j].first)
                {
                    j++;
                }
                else
                    i++;
            }
            else
            {
                firstpos = b[j].first;
                zeropos = a[i].first;
                firstposval = b[j].second;
                zeroposval = a[i].second;
                break;
            }
        }
        
        if (firstposval == zeroposval)
            firstpos = 0;
        
        if (nums.size() & 1)
        {
            int k = nums.size() / 2 + 1;
            cnt += k - zeropos;
            cnt += nums.size() / 2 - firstpos;
        }
        else
        {
            cnt += nums.size() / 2 - zeropos;
            cnt += nums.size() / 2 - firstpos;
        }
        return cnt;
    }
};