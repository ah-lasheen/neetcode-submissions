class Solution {
    public int maxProfit(int[] prices) {
        int max = 0, left = 0, right = 1;
        
        while (right < prices.length) {
            if (prices[left] < prices[right]) {
                int profit = prices[right] - prices[left];
                max = Math.max(max, profit);
            } else {
                left = right;
            }
            right++;
        }

        return max;
    }
}
