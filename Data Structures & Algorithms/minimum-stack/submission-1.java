class MinStack {
    private Stack<Integer> stack = new Stack<>();
    int min = Integer.MAX_VALUE;
    
    public void push(int val) {
        if (val <= min) {
            stack.push(min); // Store previous min before updating
            min = val;
        }
        stack.push(val);
    }
    
    public void pop() {
        if (stack.pop() == min) {
            min = stack.pop(); // Restore previous min
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return min;
    }
}
