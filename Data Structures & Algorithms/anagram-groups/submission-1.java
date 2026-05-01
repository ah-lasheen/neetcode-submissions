class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> anagrams = new HashMap<>();

        for (String str : strs) {
            int[] freq = new int[26];

            for (char curr : str.toCharArray()) {
                freq[curr - 'a']++;
            }

            String key = Arrays.toString(freq);
            anagrams.putIfAbsent(key, new ArrayList<>());
            anagrams.get(key).add(str);
        }

        return new ArrayList<>(anagrams.values());
    }
}
