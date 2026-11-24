package epi.leetcode;

import java.util.HashMap;
import java.util.Map;

public class ValidAnagram {
    public boolean isAnagram(String t, String s) {
        if (t.length() != s.length()) return false;
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : t.toCharArray()) {
            freq.merge(c, 1, Integer::sum);
        }
        for (char c : s.toCharArray()) {
            if (freq.getOrDefault(c, 0) == 0) return false;
            freq.merge(c, -1, Integer::sum);
        }
        return true;
    }
}
