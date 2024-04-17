class Solution {
public:
    int jump(vector<int>& nums) {
        if(nums.size() == 1)
            return 0;
        int jump = 0;
        int maxReach = 0;
        int nextJump = 0;
        for(int i=0 ; i<nums.size()-1 ; i++)
        {
            maxReach = max(i+nums[i], maxReach);
            if(i == nextJump)
            {
                nextJump = maxReach;
                jump += 1;
            }
        }
        return jump;
    }
};