class Solution {
public:
    unordered_map<TreeNode*, TreeNode*> maps;
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        
        maptoparent(root, NULL);
        
        unordered_set<TreeNode*> hash;
        queue<TreeNode*> q;
        int currl = 0;
        q.push(target);
        hash.insert(target);
        
        while(!q.empty()){
            if(currl == K)
                return extractfromq(q);
            int size = q.size();
            for(int i = 0; i < size; i++){
                TreeNode* curr = q.front();
                q.pop();
                
                if(curr->left && !hash.count(curr->left)){
                    hash.insert(curr->left);
                    q.push(curr->left);
                }
                if(curr->right && !hash.count(curr->right)){
                    hash.insert(curr->right);
                    q.push(curr->right);
                }
                TreeNode* parent = maps[curr];
                if(parent && !hash.count(parent)){
                    hash.insert(parent);
                    q.push(parent);
                }
            }
            currl++;
        }
        return {};
    }
    void maptoparent(TreeNode* root, TreeNode* parent){
        if(root == NULL) return;
        maps[root] = parent;
        maptoparent(root->left, root);
        maptoparent(root->right, root);
    }
    vector<int> extractfromq(queue<TreeNode*> q){
        vector<int> res;
        while(!q.empty()){
            res.push_back(q.front()->val);
            q.pop();
        }
        return res;
    }
};