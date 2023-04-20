class Solution {
public:
    vector<vector<int>> graph;
    vector<int> maxChain;
    
    int getMaxChain(int src)
    {
        if(maxChain[src]>0)
            return maxChain[src];
        maxChain[src]=1;
        for(auto child:graph[src])
        {
            maxChain[src]=max(maxChain[src],1+getMaxChain(child));
        }
        return maxChain[src];
    }
    
    int longestStrChain(vector<string>& words) {
        unordered_map<string,int> mp;
        int n=words.size();
        for(int i=0;i<n;i++)
        {
            mp[words[i]]=i;
        }
        graph.clear();
        maxChain.clear();
        graph.resize(n);
        maxChain.resize(n);
        
        for(int i=0;i<size(words);i++)
        {
            string currentString=words[i];
            for(int j=0;j<size(currentString);j++)
            {
                string removeOneCharacter = currentString.substr(0,j)+currentString.substr(j+1);
                if(!mp.count(removeOneCharacter))
                {
                    continue;
                }
                graph[i].push_back(mp[removeOneCharacter]);
            }
        }
        int maximumChain = 0;
        for(int i=0;i<n;i++)
        {
            maximumChain = max(maximumChain,getMaxChain(i));
        }
        return maximumChain;
        
    }
};