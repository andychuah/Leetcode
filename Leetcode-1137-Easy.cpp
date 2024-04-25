class Solution {
public:
    int tribonacci(int n) {
        if (n == 0) return 0; // Base case: T(0) = 0
        if (n == 1 || n == 2) return 1; // Base cases: T(1) = T(2) = 1
        
        int dp[3] = {0, 1, 1}; // Initialize array to store Tribonacci numbers
        for (int i = 3; i <= n; ++i) {
            int next = dp[0] + dp[1] + dp[2]; // Calculate next Tribonacci number
            dp[0] = dp[1]; // Update array for next iteration
            dp[1] = dp[2];
            dp[2] = next;
        }
        
        return dp[2]; // Return Tribonacci number at index n
    }
};