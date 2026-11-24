package epi.leetcode;

public class BinaryGap {
    public int binaryGap(int n) {
        String str = Integer.toBinaryString(n);
        int left = -1;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '1') {
                left = i;
                break;
            }
        }
        if (left == -1) return 0;
        for (int i = str.length() - 1; i >= 0; i--) {
            if (str.charAt(i) == '1') {
                return i - left;
            }
        }
        return 0;
    }
}
