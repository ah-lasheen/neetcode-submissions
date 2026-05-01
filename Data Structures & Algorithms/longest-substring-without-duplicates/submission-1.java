class Solution {
    public int lengthOfLongestSubstring(String s) {
        // testcase
        if (s.length() <= 1) return s.length();


        // create pointers and set to dynamically edit our window & let us keep track of chars in our substring
        Set<Character> dups = new HashSet<>();
        int left = 0, right = 0;
        int longest = Integer.MIN_VALUE;

        while (right < s.length()) {
            char curr = s.charAt(right);
            // if set does not have char, add to set and inc right to check next
            if (!dups.contains(curr)) {
                dups.add(curr);
                if (longest < (right - left + 1)) longest = right - left + 1;
                right++;
            }   
            // if set does have char, remove chars at left curr pointer & inc left until no more dups
            else if (dups.contains(curr)) {
                dups.remove(s.charAt(left));
                left++;
            }
        }

        return longest;
    }
}
