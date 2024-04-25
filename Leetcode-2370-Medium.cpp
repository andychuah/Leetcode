class Solution {
public:
    int longestIdealString(string s, int k) {
        int dp[27] = {0};
        int n = s.length();

        for(int i=n-1 ; i>=0 ; i--)
        {
            int idx = s[i] - 'a';
            int maxNum = -1;
            int left = max((idx - k), 0);
            int right = min((idx + k), 26);

            for(int j=left ; j<= right ; j++)
            {
                maxNum = max(maxNum, dp[j]);
            }
            dp[idx] = maxNum + 1;
        }

        int max = -1;
        for(int i=0 ; i<27 ; i++)
        {
            if(dp[i] > max)
                max = dp[i];
        }
        return max;
    }
};