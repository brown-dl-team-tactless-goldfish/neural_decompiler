struct TrieNode {
    TrieNode *children[26] = {NULL};
    bool endOfWord = false;
};
class Solution {
public:
    void insertWord(TrieNode *trie, string &word) {
        for (char &c : word) {
            int index = c - 'a';
            if (!trie->children[index])
                trie->children[index] = new TrieNode;
            trie = trie->children[index];
        }
        trie->endOfWord = true;
    }
    vector<string> searchWord(TrieNode *trie, string &prefix) {
        vector<string> result;
        for (char &c : prefix) {
            int index = c - 'a';
            if (!trie->children[index])
                return {};
            trie = trie->children[index];
        }
        dfs(trie, prefix, result);
        return result;
    }
    void dfs(TrieNode *trie, string pre, vector<string> &result) {
        if (result.size() == 3)
            return;
        if (trie->endOfWord)
            result.push_back(pre);
        
        for (int i = 0; i < 26; i++) {
            if (trie->children[i])
                dfs(trie->children[i], pre + (char)(i + 'a'), result);
        }
    }
    vector<vector<string>> suggestedProducts(vector<string>& products, string search) {
        TrieNode *trie = new TrieNode;
        for (string &prod : products)
            insertWord(trie, prod);
        vector<vector<string>> result;
        string prefix;
        for (char &c : search) {
            prefix += c;
            result.push_back(searchWord(trie, prefix));
        }
        return result;
    }
};