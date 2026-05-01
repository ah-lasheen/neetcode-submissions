class Solution {
    public int maxArea(int[] heights) {
        int maxWater = 0;

        int lp = 0, rp = heights.length - 1;

        while (lp < rp) {
            int leftHeight = heights[lp], rightHeight = heights[rp];
            int currWater = (rp - lp) * Math.min(leftHeight, rightHeight); // width x height
            if (currWater > maxWater) {
                // setting new maxWater  
                maxWater = currWater;
            } 
            // imp that pointer needs to move, move the smaller heights[i] pointer
            else if (leftHeight <= rightHeight) { 
                lp++;
            }
            else {
                rp--;
            }
        }

        return maxWater;
    }
}
