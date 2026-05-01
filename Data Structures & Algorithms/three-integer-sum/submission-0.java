class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // keys = array of sorted triplets (strings), values = list of triplets
        Map<String, List<Integer>> map = new HashMap<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            // create left and right pointer
            int lp = i + 1;
            int rp = nums.length - 1;

            while (lp < rp) {
                int sum  = nums[i] + nums[lp] + nums[rp];

                if ((i != lp && lp != rp) && (sum == 0)) {
                    int[] tripletArray = {nums[i], nums[lp], nums[rp]};
                    // in case another combination of i, lp, rp, comes to add into matrix
                    // now we can easily see mutations of i, lp, rp and use putIfAbsent
                    String finalTripletKey = Arrays.toString(tripletArray);

                    List<Integer> finalTripletList = Arrays.stream(tripletArray).boxed().collect(Collectors.toList());

                    map.putIfAbsent(finalTripletKey, finalTripletList);

                    lp++;
                    rp--;
                } else if (sum < 0) { // move left pointer to right to inc sum
                    lp++;
                } else { // move right pointer to left to dec sum
                    rp--;   
                }  
            } 
        }

        return new ArrayList<>(map.values());
    }
}
