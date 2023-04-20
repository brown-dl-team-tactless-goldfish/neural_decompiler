/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct pair {
    int parent;
    int level;
};
void find(struct TreeNode* root, int parent,int target,struct pair *pp,int level) {
    level++;
    if(root->val == target) {
     pp->level = level;
     pp->parent = parent;
    }

    if(root->left) find(root->left,root->val,target,pp,level);
    if(root->right)find(root->right,root->val,target,pp,level);
} 
bool isCousins(struct TreeNode* root, int x, int y){
  struct pair xd;
  struct pair yd;
    xd.parent =0,yd.parent =0;
    xd.level = 0,yd.level =0;
    find(root,0,x,&xd,0);
    find(root,0,y,&yd,0);
   // printf("%d %d\n",xd.level,yd.level);
   // printf("%d %d\n",xd.parent,yd.parent);
    if(xd.parent!=yd.parent && xd.level == yd.level) return true;
    return false;
}