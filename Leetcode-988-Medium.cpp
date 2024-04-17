/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    string smallestFromLeaf(TreeNode* root) {
        string result;
        dfs(root, "", result);
        return result;
    }

    void dfs(TreeNode* node, string path, string& smallest)
    {
        if(!node)
            return;
        
        path += char('a' + node->val);

        if(!node->left && !node->right) //leaf node
        {
            reverse(path.begin(), path.end());
            if(smallest > path || smallest.empty())
            {
                smallest = path;
            }
            reverse(path.begin(), path.end());
        }
        dfs(node->left, path, smallest);
        dfs(node->right, path, smallest);
    }


};