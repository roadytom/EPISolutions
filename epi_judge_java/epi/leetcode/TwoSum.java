package epi.leetcode;

import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> memo = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (memo.containsKey(target - nums[i])) {
                return new int[]{memo.get(target - nums[i]), i};
            }
            memo.put(memo.get(i), i);
        }
        return new int[]{};
    }
}
