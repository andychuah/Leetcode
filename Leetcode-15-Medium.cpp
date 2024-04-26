class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());

        for(int i=0 ; i<nums.size() ; i++)
        {
            if(i > 0 && nums[i] == nums[i-1])
                continue;

            int j = i + 1;
            int k = nums.size() - 1;
            while(j < k)
            {
                int curr_sum = nums[i] + nums[j] + nums[k];
                if(curr_sum == 0)
                {
                    res.push_back({nums[i], nums[j], nums[k]});
                    j += 1;
                    while(nums[j] == nums[j-1] && j < k)
                    {
                        j += 1;
                    }
                }
                else if(curr_sum > 0)
                {
                    k -= 1;
                }
                else if(curr_sum < 0)
                {
                    j += 1;
                }
            }
        }
        return res;
    }
};