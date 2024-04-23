class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        // Step 1: Preprocess to compute heights of consecutive ones for each cell
        for (int j = 0; j < n; ++j) {
            for (int i = 1; i < m; ++i) {
                if (matrix[i][j] == 1)
                    matrix[i][j] += matrix[i - 1][j];
            }
        }

        // Step 2: Calculate maximum area for each cell
        int maxArea = 0;
        for (int i = 0; i < m; ++i) {
            std::sort(matrix[i].begin(), matrix[i].end(), std::greater<int>());
            for (int j = 0; j < n; ++j) {
                maxArea = std::max(maxArea, matrix[i][j] * (j + 1));
            }
        }

        return maxArea;
    }
};