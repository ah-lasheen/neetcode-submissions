class Solution {
    public boolean isPalindrome(String s) {
        if (s.length() <= 1) {
            return true;
        }

        s = s.toLowerCase();
        int leftP = 0, rightP = s.length() - 1;

        while (leftP < rightP) {
            while (leftP < rightP && !Character.isLetterOrDigit(s.charAt(leftP))) {
                leftP++; 
            }
            while (leftP < rightP && !Character.isLetterOrDigit(s.charAt(rightP))) {
                rightP--;
            }   

            if (s.charAt(leftP) != s.charAt(rightP)) {
                return false;
            }

            leftP++;
            rightP--;
        }

        return true;
    }
}