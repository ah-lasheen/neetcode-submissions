class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;

        while (l <= r) {
            int m = (l + r) / 2;
            
            // check for if midpoint = target
            if (target == nums[m]) return m;

            // checking which side to sort through
            // if nums[l] <= nums[m], search left tree
            if (nums[l] <= nums[m]) {
                // find out where to reset bounds in left tree
                // if nums[l] <= target < nums[m], target is in the left subarray
                if (nums[l] <= target && target < nums[m]) {
                    r = m - 1;
                }
                // otherwise in right subarray
                else {
                    l = m + 1;
                }
            } 
            // search right tree
            else {
                // find out where to reset bounds in left tree
                // if nums[m] < target <= nums[r], target is in the right subarray
                if (nums[m] < target && target <= nums[r]) {
                    l = m + 1;
                }
                // otherwise in left subarray
                else {
                    r = m - 1;
                }
            }
        }
        return -1;
    }
}
