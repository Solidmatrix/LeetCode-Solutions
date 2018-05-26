class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length()-1;
        int ll, rr, diff;
        while (left < right){
            ll = s.charAt(left);
            rr = s.charAt(right);
            while (ll < 48 || (ll > 57 && ll < 65) || (ll > 90 && ll < 97) || ll > 122) {
                if (++left >= right) return true;
                ll = s.charAt(left);
            }
            while (rr < 48 || (rr > 57 && rr < 65) || (rr > 90 && rr < 97) || rr > 122) {
                if (--right <= left) return true;
                rr = s.charAt(right);
            }
            diff = ll - rr;
            if (diff != 0 && diff != 32 && diff != -32) return false;
            if ((ll <= 57 && rr >= 65) || (rr <= 57 && ll >= 65)) return false;
            ++left;
            --right;
        }
        return true;
    }
}