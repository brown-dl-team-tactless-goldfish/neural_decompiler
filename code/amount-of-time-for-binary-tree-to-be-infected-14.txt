class Solution 
{
public:
    int timetoinfect(TreeNode* target, map<TreeNode*, TreeNode*> parent)
    {
        map<TreeNode*, bool> visited;
        queue<TreeNode*> q;
        q.push(target);
        visited[target] = true;
        int time=0;
        while(!q.empty())
        {
            int size = q.size(), fl=0;

            for(int i=0; i<size; i++)
            {
                TreeNode* current = q.front(); q.pop();
                visited[current] = true;

                if(current->left && !visited[current->left])
                {
                    fl =1;
                    q.push(current->left);
                    visited[current->left] = true;
                }

                if(current->right && !visited[current->right])
                {
                    fl=1;
                    q.push(current->right);
                    visited[current->right] = true;
                }

                if(parent[current] && !visited[parent[current]])
                {
                    fl=1;
                    q.push(parent[current]);
                    visited[parent[current]] = true;
                }
            }
            if(fl) time++;
        }
        return time;
    }
   TreeNode* makeParent(TreeNode* root, map<TreeNode*, TreeNode*> &parent, int start)
    {
        TreeNode* target;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty())
        {
            TreeNode* node = q.front();
            q.pop();
            if(node->val == start) 
                target = node;
            if(node->left)
            {
                q.push(node->left);
                parent[node->left] = node;
            }
            if(node->right)
            {
                q.push(node->right);
                parent[node->right] = node;
            }
        }
        return target;
    }
    int amountOfTime(TreeNode* root, int start) 
    {
        map<TreeNode*, TreeNode*> parent;
        TreeNode* target = makeParent(root, parent, start);
        int maxi = timetoinfect(target, parent);
        return maxi;
        
    }
};