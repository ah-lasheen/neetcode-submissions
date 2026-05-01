class Solution {
    public boolean hasDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int val = nums[i];
            int count = i;
            while ((count + 1) < nums.length) {
                int test = nums[count + 1];
                if (val == test) {
                    return true;
                }
                count++;
            }
        }
        return false;
    }
}
