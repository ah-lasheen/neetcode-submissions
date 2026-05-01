class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int lRow = 0, rRow = matrix.length - 1;
        int lCol = 0, rCol = matrix[0].length - 1;
        int row = -1;

        while (lRow <= rRow) {
            int mRow = (lRow + rRow) / 2;
            
            // if matrix[mRow][lCol] <= target <= matrix[mRow][rCol], target in mRow
            if ((matrix[mRow][lCol] <= target) && (target <= matrix[mRow][rCol])) {
                // iterate through columns in next while loop
                row = mRow;
                break;
            } 
            // if target < matrix[mRow][lCol], lRow <= targetRow < mRow: rRow = mRow - 1; 
            else if (target < matrix[mRow][lCol]) {
                rRow = mRow - 1;
            }
            // mRow + 1 <= target <= rRow: lRow = mRow + 1
            else {
                lRow = mRow + 1;
            }
        }

        // check if no valid row was found
        if (row == -1) return false;

        // iterate through cols now to find target in row
        while (lCol <= rCol) {
            int mCol = (lCol + rCol) / 2;

            // if target = mCol of row, return true
            if (target == matrix[row][mCol]) {
                return true;
            }
            // if target < mCol, rCol = mCol - 1
            else if (target < matrix[row][mCol]) {
                rCol = mCol - 1; // search left half
            }
            // if target > mCol, lCol = mCol + 1
            else {
                lCol = mCol + 1; // search right half
            }
        }

        return false;
    }
}
