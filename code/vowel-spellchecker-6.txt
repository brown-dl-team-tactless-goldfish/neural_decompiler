class Solution {
    bool isVowel(char ch)
    {
        if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch =='u' || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U')
            return true;
        return false;
    }
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries)
    {
        unordered_map<string, int> list;
        unordered_map<string, int> cases;
        set<string> sfst;
        int idx = 0;
        for(string &word : wordlist)
        {
            sfst.insert(word);
            string str = "";
            string w = "";
            int slen = word.size();
            for(int i = 0; i < slen; i++)
            {
                
                if(isVowel(word[i]))
                    str += '*';
                else
                {
                    str += tolower(word[i]);
                }
                w += tolower(word[i]);
            }
            if(!list.count(str))
                list[str] = idx;
            if(!cases.count(w))
                cases[w] = idx;
            idx++;
        }
        int n = queries.size();
        for(int i = 0; i < n; i++)
        {
            string str = "", w = "";
            int slen = queries[i].size();
            if(sfst.find(queries[i]) != sfst.end())
            {
                continue;
            }
            for(int j = 0; j < slen; j++)
            {

                if(isVowel(queries[i][j]))
                    str += '*';
                else
                {
                    str += tolower(queries[i][j]);
                }
                w += tolower(queries[i][j]);
            }
            if(cases.count(w))
            {
                queries[i] = wordlist[cases[w]];
                continue;
            }
            if(list.count(str))
            {
                queries[i] = wordlist[list[str]];
                continue;
            }
            queries[i] = "";
        }
        return queries;
    }
};