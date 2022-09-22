package BruteForce;

class Solution {
    public String reverseWords(String s) {
        String res = new String("");
        String[] strs = s.split(" ");
        for (String str: strs) {
            res += reverseWord(str);
            res += " ";
        }
        res = res.substring(0, res.length() - 1);
        return res;
        
    }

    public String reverseWord(String str) {
        String res = new String("");
        for (int i = str.length() - 1; i >= 0; i--) {
            res += str.charAt(i);
        }
        return res;
    }
}