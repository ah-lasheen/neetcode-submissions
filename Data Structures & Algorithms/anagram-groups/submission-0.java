class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // map to collect all strings (in array form) and respective list collection of anagrams
        // key = String, value = list of 
        Map<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            // creating frequency array for key of map for each str in strs
            int[] freqArr = new int[26];
            // frequency array edited
            for (char ch : str.toCharArray()) {
                freqArr[ch - 'a']++;
            }

            // if string freqency array doesnt already exist, create an empty one
            String key = Arrays.toString(freqArr);
            map.putIfAbsent(key, new ArrayList<>());

            // add current str to existing list associated with freqArr
            map.get(key).add(str);
        }

        return new ArrayList<>(map.values());
    }
}
