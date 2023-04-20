class Solution {
public:
    class Trie {
    public:
        Trie() {
            cnt = 0;
            for(int i=0;i<26;i++){
                this->next[i] = NULL;
            }
        }
        void insert(string word, Trie* root) {
            Trie* node = root;
            int i = 0;
            for (char ch : word) {
                ch -= 'a';
                if (!node->next[ch]) { node->next[ch] = new Trie(); }
                node->next[ch]->cnt++;
                node = node->next[ch];
                i++;
            }
        }

        int search(char ch, Trie* node) {
            return node->next[ch-'a']->cnt;
        }

        Trie* next[26] = {};
        int cnt;
    };
    vector<int> sumPrefixScores(vector<string>& words) {
        Trie t;
        Trie *root = new Trie();
        int n = words.size();
        for(int i=0;i<n;i++){
            t.insert(words[i], root);
        }
        vector<int> ans;
        for(int i=0;i<n;i++){
            string cur = "";
            int c = 0;
            Trie *node = root;
            for(int j=0;j<words[i].length();j++){
                c += t.search(words[i][j], node);;
                if(node->next[words[i][j]-'a'] == NULL) break;
                node = node->next[words[i][j]-'a'];
            }
            ans.push_back(c);
        }
        return ans;
    }
};
