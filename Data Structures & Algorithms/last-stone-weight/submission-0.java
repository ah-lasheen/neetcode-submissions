class Solution {
    public int lastStoneWeight(int[] stones) {
        if (stones.length == 1) return stones[0];
        
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (int stone : stones) {
            maxHeap.offer(stone);
        }

        while (maxHeap.size() > 1) {
            int w1 = maxHeap.poll();
            int w2 = maxHeap.poll();

            // if stones do not weight the same, must offer back the difference of weight
            // ( w1 != w2 ) implies that w1 > w2 since maxHeap
            if (w1 != w2) {
                maxHeap.offer(w1 - w2);
            }
        }

        return (maxHeap.size() == 0) ? 0 : maxHeap.peek();
    }
}
