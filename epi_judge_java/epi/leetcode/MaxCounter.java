package epi.leetcode;

import java.util.Arrays;

public class MaxCounter {
    public int[] solution(int N, int[] A) {
        int[] ans = new int[N];
        int maxCnt = 0;
        int toAdd = 0;
        for (int x : A) {
            if (1 <= x && x <= N) {
                ans[x - 1] = Math.max(toAdd, ans[x - 1]);
                ans[x - 1]++;
                maxCnt = Math.max(maxCnt, ans[x - 1]);
            } else {
                toAdd = maxCnt;
            }
        }
        for (int i = 0; i < N; i++) {
            ans[i] = Math.max(ans[i], toAdd);
        }
        return ans;
    }

    public static void main(String[] args) {
        var a = new MaxCounter();
        System.out.println(Arrays.toString(a.solution(5, new int[]{3, 4, 4, 6, 1, 4, 4})));
    }
}

