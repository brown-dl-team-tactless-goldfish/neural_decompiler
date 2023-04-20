class Solution
{
	public:
    unordered_map<string, vector<string>> g;

    vector<string> findAllRecipes(vector<string> &recipes, vector<vector<string>> &ingredients, vector<string> &supplies)
    {
        g.clear();
		// Dependancy manager 
        map<string, int> indegree;

       
        for (int i = 0; i < ingredients.size(); i++)
        {
            for (string s : ingredients[i])
            {
				// recpes[i] : Hey, I need s to make me so add me to its list(adjecency list)
                g[s].push_back(recipes[i]);
                indegree[recipes[i]]++;
            }
        }

        queue<string> q;
        
        for(string item : supplies)
        {
			// Hey I dont need any other item to made me, I am alone and can help making others
			  q.push(item);
            
        }

        while(!q.empty())
        {
            string current = q.front();
            q.pop();

            for(string recipe : g[current])
            {
                indegree[recipe]--;
				// Hey wooo!!!, I got all my supplies now I can be used for making other recepies
                if(indegree[recipe] == 0)
                {
                    q.push(recipe);
                }
            }
        }

        vector<string> ans;
        for(string recipe : recipes)
        {
			// Hey, I just made it to the final!!!!! :)
            if(indegree[recipe] == 0)
            {
                ans.push_back(recipe);
            }
        }
        return ans;
    }
};