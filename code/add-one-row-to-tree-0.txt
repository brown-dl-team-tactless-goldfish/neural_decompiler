struct TreeNode* addOneRow(struct TreeNode* root, int val, int depth){
    if(depth == 1){
        struct TreeNode* NewRoot = malloc(sizeof(struct TreeNode));
        NewRoot->val =  val;
        NewRoot->left = root;
        NewRoot->right = NULL;
        root = NewRoot;
        return root;
    }
    
    if(depth == 2){
        struct TreeNode* leftNode = malloc(sizeof(struct TreeNode));
        leftNode->val =  val;
        struct TreeNode* rightNode = malloc(sizeof(struct TreeNode));
        rightNode->val =  val;
        leftNode->left = root->left;
        leftNode->right = NULL;
        rightNode->right = root->right;
        rightNode->left = NULL;
        root->left = leftNode;
        root->right = rightNode;
        return root;
    }
    
    if(root->left){
        addOneRow(root->left, val, depth-1);    
    }
    if(root->right){
        addOneRow(root->right, val, depth-1);    
    }
    
    return root;

}