class Solution {
public:
    bool canJump(vector<int>& nums) {
         if (nums.size() == 1)
            return true;

        int maxReach = nums[0]; // Initialize maxReach with the first element
        int i = 1; // Start from the second element of the array

        while (i <= maxReach && i < nums.size()) { 
            // Iterate until maxReach or end of array is reached
            maxReach = max(maxReach, i + nums[i]);
            if (maxReach >= nums.size() - 1)
                return true;
            i++; // Move to the next position
        }

        return false;
    }
};