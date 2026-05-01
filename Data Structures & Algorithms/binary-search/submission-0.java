class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;

        while (l <= r) {
            int m = (l + r) / 2;

            if (target == nums[m]) return m;

            // if target = nums[m], search left subarray
            if (target < nums[m]) {
                r = m - 1;
            }
            // otherwise target > nums[m], search right subarray
            else {
                l = m + 1;
            }
        }

        return -1; 
    }
}
