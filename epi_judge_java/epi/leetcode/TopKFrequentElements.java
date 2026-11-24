package epi.leetcode;

import java.util.*;

public class TopKFrequentElements {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.merge(num, 1, Integer::sum);
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] == b[0]) return a[1] - b[1];
            return b[0] - a[0];
        });
        for (var entry : freq.entrySet()) {
            pq.offer(new int[]{entry.getValue(), entry.getKey()});
        }
        List<Integer> ans = new ArrayList<>();

        while (k != 0 && !pq.isEmpty()) {
            int[] curr = pq.poll();
            ans.add(curr[1]);
            k--;
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}
