class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rl = 0, rr = matrix.length - 1;
        int cl = 0, cr = matrix[0].length - 1;

        while (rl <= rr) {
            int rm = (rl + rr) / 2;
            // check 
            //  if target < first i of rm && target < first i of rr
            //      then target is within rm and break
            //  else if target < first i of rm
            //      then r = m - 1;
            //  else if target > last i of rm
            //      then l = m + 1
            if (matrix[rm][0] <= target && target <= matrix[rm][cr]) {
                rl = rm;
                break;
            }
            else if (target < matrix[rm][cr]) {
                rr = rm - 1;
            }
            else if (target > matrix[rm][cl]) {
                rl = rm + 1;
            }
        }

        if (rl < 0 || rl >= matrix.length) return false;

        // instantiate targetRow
        int[] targetR = matrix[rl];

        // binary search through cols of rm
        while (cl <= cr) {
            int m  = (cl + cr) / 2;
            // check
            //  if target == targetR[m]
            //      then return true;
            //  else if targetR[cl] < m
            //      then m = cr - 1
            //  else if targetR[c] > m
            //      then m = cl + 1
            if (target == targetR[m]) {
                return true;
            }
            else if (targetR[m] < target) {
                cl = m + 1;
            }
            else {
                cr = m - 1;
            }
        }

        return false;
    }
}
