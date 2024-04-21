class Solution {
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        int row = land.size();
        int col = land[0].size();
        vector<vector<int>> ans;
        for(int i=0 ; i<row ; i++)
        {
            for(int j=0 ; j<col ; j++)
            {
                int maxRow = i;
                int maxCol = j;
                if(land[i][j] == 1)
                {
                    dfs(land, maxRow, maxCol, i, j);
                    ans.push_back({i, j, maxRow, maxCol});
                }
            }
        }
        return ans;
    }

    void dfs(vector<vector<int>>& land, int& maxRow, int& maxCol, int i, int j)
    {
        if(i >= land.size() || j >= land[0].size() || land[i][j] != 1)
            return;

        land[i][j] = 0;
        maxRow = max(maxRow, i);
        maxCol = max(maxCol, j);
        dfs(land, maxRow, maxCol, i+1, j); //down
        dfs(land, maxRow, maxCol, i, j+1); //right

    }
};