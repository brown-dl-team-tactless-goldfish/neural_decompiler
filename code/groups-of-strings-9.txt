class Solution {
private:
    int grp_cnt, max_size;
    vector<int> parent, rank;
    
    int get_mask(string &word) {
        int mask = 0;
        for(char ch: word) 
            mask = mask | (1<<(ch-'a'));
        return mask;
    }
    
    int find(int x) {
        if(parent[x] == -1)
            return x;
        return parent[x] = find(parent[x]);
    }
    
    void merge(int x, int y) {
        x = find(x);
        y = find(y);
        
        if(x == y)
            return;
        else if(rank[x] < rank[y])
            swap(x, y);
        
        parent[y] = x;
        rank[x] += rank[y];
        
        grp_cnt -= 1;
        max_size = max(max_size, rank[x]);
    }
    
public:
    vector<int> groupStrings(vector<string>& words) {
        int n = words.size();
        grp_cnt = n;
        max_size = 1;
        
        parent = vector<int>(n, -1);
        rank = vector<int>(n, 1);
        
        // {mask, index}
        // map<int, int> index_of;
        unordered_map<int, int> index_of;
        
        
        vector<int> mask(n, 0);
        for(int i = 0; i < n; i++) {
            mask[i] = get_mask(words[i]);
            index_of[mask[i]] = i;
        }
        
        for(int i = 0; i < n; i++) {
            // duplicate word "ab", "ba"
            merge(i, index_of[mask[i]]);
            for(char ch: words[i]) {
                // removing ch (removing complements the adding)
                int without = mask[i] ^ (1 << (ch-'a'));
                if(index_of.count(without)) 
                    merge(i, index_of[without]);
                
                // replacing ch with any other character
                for(int j = 0; j < 26; j++) {
                    if(j == ch-'a')
                        continue;
                    int withreplace = without | (1<<j); 
                    if(index_of.count(withreplace)) 
                        merge(i, index_of[withreplace]);
                }
            }
        }
        
        return {grp_cnt, max_size};
    }
};


