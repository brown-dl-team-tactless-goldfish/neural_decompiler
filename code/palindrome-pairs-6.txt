struct TrieNode{
    TrieNode *children[26];
    int index;
    TrieNode() : index(-1) {
        for(int i = 0; i < 26; i++) {
            children[i] = NULL;
        }
    }
};

void insert(TrieNode* root, string s, int i) {
    // first reverse and add strings into trie.
    reverse(s.begin(), s.end());
    TrieNode *ptr = root;
    for(char c : s) {
        int index = c - 'a';
        if(!ptr->children[index]) {
            ptr->children[index] = new TrieNode();
        }
        ptr = ptr->children[index];
    }
    // index of string.
    ptr->index = i;
    return;
}

void find(TrieNode* root, vector<int> &palindromes, string s = "") {
    // base condition, if formed string is a palindrome or not.
    if(root->index != -1) {
        int i = 0, j = s.length() - 1;
        //cout<<s<<endl;
        bool flag = true;
        while(i <= j) {
            if(s[i] != s[j]) {
                flag = false;
                break;
            }
            i++;
            j--;
        }
        if(flag)
            palindromes.push_back(root->index);
    }
    for(int i = 0; i < 26; i++) {
        if(root->children[i]) {
            char c = 'a' + i;
            s.push_back(c);
            find(root->children[i], palindromes, s);
            s.pop_back();
        }
    }
    return;
}

vector<int> search(TrieNode* root, string s) {
    vector<int> palindromes;
    TrieNode* ptr = root;
    for(int i = 0; i < s.length(); i++) {
        char c= s[i];
        int index = c - 'a';
        // If any strings ends here, then check if out left out string is palindrome or not.
        if(ptr->index != -1) {
            int j = i, k = s.length() - 1;
            bool flag = true;
            while(j <= k) {
                if(s[j] != s[k]) {
                    flag = false;
                    break;
                }
                j++;
                k--;
            }
            if(flag)
                palindromes.push_back(ptr->index);
        }
        // If no characters ahead matching.
        if(!ptr->children[index]) {
            return palindromes;
        }
        ptr = ptr->children[index];
    }
    find(ptr, palindromes);
    return palindromes;
}

class Solution {
public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        struct TrieNode* root = new TrieNode();
        int i = 0;
        for(string s : words) {
            // insert into trie.
            insert(root, s, i++);
        }
        vector<vector<int>> result;
        i = 0;
        for(string s : words) {
            // search for all palindromes.
            vector<int> palindromes = search(root, s);
            //cout<<s<<endl;
            // add all palindromes into result.
            for(int x : palindromes) {
                if(i != x)
                    result.push_back({i, x});
            }
            i++;
        }
        return result;
    }
};