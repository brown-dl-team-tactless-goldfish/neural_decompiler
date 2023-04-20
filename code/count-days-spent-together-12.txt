class Solution
{
public:
    vector<int> v = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int solve(string s)
    {
        int m = (s[0] - '0') * 10 + (s[1] - '0');
        int d = (s[3] - '0') * 10 + (s[4] - '0');
        m--;
        while (m > 0)
        {
            d += v[m];
            m--;
        }
        return d;
    }
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob)
    {
        int a0 = solve(arriveAlice);
        int a1 = solve(leaveAlice);
        int b0 = solve(arriveBob);
        int b1 = solve(leaveBob);
        int ans = 0;
        for (int i = 0; i < 366; i++)
            if ((i >= a0 && i <= a1) && (i >= b0 && i <= b1))
                ans++;
        return ans;
    }
};