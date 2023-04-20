class Solution {
public:
    vector<int> longestRepeating(string s, string queryCharacters, vector<int>& queryIndices) {
        auto root = Node(s, 0, s.size());
        vector<int> res;
        for(int i=0;i< queryCharacters.size(); i++){
            root.change( queryCharacters[i], queryIndices[i]);
            res.push_back(root.maxLen);
        }
        return res;
    }
    
    struct Node{   
        Node(const string& s, int al, int ar) : l(al), r(ar), n(r-l){
            if (l+1 == r){
                cLeft = cRight = s[l];
                lenLeft = lenRight = maxLen = 1;
                isFull = true;
                return;
            }
            
            auto mid = (l + r) / 2;
            pl = new Node(s, l, mid);
            pr = new Node(s, mid, r);            
            update();                        
        }
        
        //when child changed
        void update(){
            cLeft = pl->cLeft;
            cRight = pr->cRight;
            
            lenLeft = pl->lenLeft;
            if(pl->isFull && pl->cLeft == pr->cLeft) lenLeft += pr->lenLeft;
            
            lenRight = pr->lenRight;
            if(pr->isFull && pl->cRight == pr->cLeft) lenRight += pl->lenRight;
            
            isFull = (lenLeft == n);            
            
            maxLen = max(pl->maxLen, pr->maxLen);
            if(pl->cRight == pr->cLeft) maxLen = max(maxLen, pl->lenRight + pr->lenLeft);
        }        
        
        void change(char c, int pos){
            if(l == r-1){
                assert(l == pos);
                cLeft = cRight = c;
                return;
            }
            
            auto mid = (l + r) / 2;
            (pos < mid ? pl : pr)->change(c, pos);
            update();            
        }
        
        const int l;
        const int r;
        const int n;
        bool isFull;
        int lenLeft;
        int lenRight;
        int maxLen;
        char cLeft;
        char cRight;
        Node* pl = nullptr;
        Node* pr = nullptr;
    };
};