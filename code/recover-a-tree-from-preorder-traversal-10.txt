class Solution {
public:
    int i=0;
    TreeNode* recoverFromPreorder(string &S,int d)
    {
        int nextDigitPos=S.find_first_of("1234567890",i);                          // Get index of the first number after i.
        if(nextDigitPos-i!=d)                                                      // If number of '-' in between != depth return NULL
            return NULL;
        int nextDashPos=S.find("-",nextDigitPos);                                  // Get the index of the next '-'
        int rootValue=stoi(S.substr(nextDigitPos,nextDashPos-nextDigitPos));
        TreeNode* root=new TreeNode(rootValue);                                    // Create the root with the node's value
        i=nextDashPos;                                                             // Move index forward for future recursions.
        root->left=recoverFromPreorder(S,d+1);                                     // Create left subtree
        root->right=recoverFromPreorder(S,d+1);                                    // Create right subtree
        return root;
    }
    TreeNode* recoverFromPreorder(string S)
    {
        return recoverFromPreorder(S,0);
    }
};