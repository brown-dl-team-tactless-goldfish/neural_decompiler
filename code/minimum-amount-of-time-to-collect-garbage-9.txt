class Solution
{
public:
	int garbageCollection(vector<string> &garbage, vector<int> &travel)
	{
		int answer = 0;
		int k = 0;
		int mSum = -1, gSum = -1, pSum = -1;
		for (int i = 1; i < travel.size(); i++)
		{

			travel[i] = travel[i - 1] + travel[i];
		}
		for (auto x : garbage)
		{
			for (auto c : x)
			{
				answer++;
				if (c == 'M')
					mSum = k;
				if (c == 'P')
					pSum = k;
				if (c == 'G')
					gSum = k;
			}
			k++;
		}
		answer += ((gSum > 0) ? travel[gSum - 1] : 0);
		answer += ((mSum > 0) ? travel[mSum - 1] : 0);
		answer += ((pSum > 0) ? travel[pSum - 1] : 0);
		return answer;
	}
};