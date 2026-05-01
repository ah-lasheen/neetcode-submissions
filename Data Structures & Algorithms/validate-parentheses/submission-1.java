class Solution {
    public boolean isValid(String s) {
        boolean result = true;
        Stack<Character> st = new Stack<>();

        for (char curr : s.toCharArray()) {
            // check if curr is an open bracket, if it is, add to stack
            if (curr == '(' || curr == '[' || curr == '{') {
                st.push(curr);
            }
            // curr is a closing bracket, see if matches top of the stack
            else {
                // if nothing in stack at first iteration, first char in s is a closing bracket,
                // therefore: false
                if (st.empty()) return false;

                // otherwise, top = st.peek() and check for matching pairs
                char top = st.peek();

                // check for matching pairs
                if ((curr == ')' && top == '(') || (curr == ']' && top == '[') || (curr == '}' && top == '{')) {
                    st.pop();
                } 
                // else, mismatched closing bracket
                else {
                    return false;
                }
            }
        }

        return st.empty();
    }
}
