class Solution {
    public int pow(int digit) {
        int result = 1;
        for (int i=0; i<digit; ++i){
            result *= 10;
        }
        return result;
    }
    
    public int countDigitOne(int n) {
        if (n < 0) return 0;
        int left, right, digit, mid, sum;
        right = 0;
        digit = -1;
        sum = 0;
        while(n != 0){
            ++digit;
            left = n / 10;
            mid = n % 10;
            if (mid == 0) sum += left * pow(digit);
            else if (mid == 1) sum += left * pow(digit) + (right + 1);
            else sum += (left + 1) * pow(digit);
            right += mid * pow(digit);
            n = left;
        }
        return sum;
    }
}