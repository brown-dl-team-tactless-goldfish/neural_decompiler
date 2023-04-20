struct Trie {
  Trie(): nodes(26) {}
  ~Trie() { 
    for (auto* node : nodes)
      delete node;
  }
  vector<Trie*> nodes;
  vector<const string*> words;  
  
  static void addWord(Trie* root, const string& word) {    
    for (char c : word) {      
      if (root->nodes[c - 'a'] == nullptr) root->nodes[c - 'a'] = new Trie();
      root = root->nodes[c - 'a'];
      if (root->words.size() < 3)
        root->words.push_back(&word);
    }
  }
  
  static vector<vector<string>> getWords(Trie* root, const string& prefix) {
    vector<vector<string>> ans(prefix.size());
    for (int i = 0; i < prefix.size(); ++i) {
      char c = prefix[i];
      root = root->nodes[c - 'a'];
      if (root == nullptr) break;
      for (auto* word : root->words)
        ans[i].push_back(*word);
    }
    return ans;
  }
};
 
class Solution {
public:
  vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
    std::sort(begin(products), end(products));
    Trie root;
    for (const auto& product : products)
      Trie::addWord(&root, product);
    return Trie::getWords(&root, searchWord);
  }
};