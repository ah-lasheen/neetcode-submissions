class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Double> minHeap = new PriorityQueue<>();
        Map<Double, List<int[]>> distanceMap = new HashMap<>();

        // Compute distances and store corresponding points
        for (int[] currPoint : points) {
            int x = currPoint[0], y = currPoint[1];
            double distance = Math.sqrt(x * x + y * y);

            minHeap.offer(distance); // Store distance in minHeap
            
            // Store points in a map, grouping them by distance
            distanceMap.putIfAbsent(distance, new ArrayList<>());
            distanceMap.get(distance).add(currPoint);
        }

        // Retrieve k closest points
        List<int[]> smallestPoints = new ArrayList<>();
        while (smallestPoints.size() < k) {
            double closestDist = minHeap.poll(); // Get the smallest distance
            smallestPoints.addAll(distanceMap.get(closestDist)); // Add corresponding points
        }

        // Convert List<int[]> to int[][] array
        int[][] result = new int[k][2];
        for (int i = 0; i < k; i++) {
            result[i] = smallestPoints.get(i);
        }

        return result;
    }
}
