package BruteForce;

import java.lang.Math;

class Solution {
    public int concatenatedBinary(int n) {
        StringBuffer buffer = new StringBuffer();
        int ans = 0;
        int mod = (int)1e9+7;
        for(int i=1; i<=n; i++) {
            buffer.append(Integer.toBinaryString(i));
        }
        for(int i=0; i < buffer.length(); i++) {
            if(buffer.charAt(i) == '1') {
                ans += Math.pow(2, i);
            }
        }
        return ans % mod;
    }
}
