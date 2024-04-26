class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        int n = grid.size();
        
        // Dynamic programming table to store the minimum sum of falling paths
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Copy the first row of the grid to dp
        for (int j = 0; j < n; ++j) {
            dp[0][j] = grid[0][j];
        }
        
        // Iterate over each row starting from the second row
        for (int i = 1; i < n; ++i) {
            // Iterate over each column in the current row
            for (int j = 0; j < n; ++j) {
                // Initialize the minimum sum for the current cell to infinity
                int min_sum = numeric_limits<int>::max();
                // Iterate over each column in the previous row
                for (int k = 0; k < n; ++k) {
                    // Avoid choosing the same column in adjacent rows
                    if (j != k) {
                        min_sum = min(min_sum, dp[i - 1][k]);
                    }
                }
                // Update the minimum sum for the current cell by adding the value from the grid
                dp[i][j] = min_sum + grid[i][j];
            }
        }
        
        // Find the minimum sum in the last row of dp
        int min_path_sum = numeric_limits<int>::max();
        for (int j = 0; j < n; ++j) {
            min_path_sum = min(min_path_sum, dp[n - 1][j]);
        }
        return min_path_sum;
    }
};