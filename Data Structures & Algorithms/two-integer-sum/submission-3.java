class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[]{0,0};
        // key = num, val = index
        Map<Integer, Integer> m = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];

            if (m.containsKey(difference)) {
                result[0] = m.get(difference);
                result[1] = i;
                return result;
            }

            m.put(nums[i], i);
        }

        return result;
    }
}
