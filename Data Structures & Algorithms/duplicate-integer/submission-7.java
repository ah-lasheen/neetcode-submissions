class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean result = false;
        int count = 0;
        Set<Integer> s = new HashSet<>();

        while (!result && count < nums.length) {
            if (!s.contains(nums[count])) {
                s.add(nums[count]);
            }
            else {
                result = true;
            }
            count++;
        }

        return result;
    }
}
