class Solution {
    public int findMin(int[] nums) {
        int l = 0;           // start
        int r = nums.length - 1; // end

        while (l < r) {
            int m = (l + r) / 2; // index of midpoint

            // if nums[m] > nums[r] we know to search right half
            if (nums[m] > nums[r]) {
                l = m + 1;
            }
            // otherwise we know to search left half
            else {
                r = m;
            }
        }

        // just to compile code
        return nums[l];
    }
}
