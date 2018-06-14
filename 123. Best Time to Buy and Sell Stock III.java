class Solution {
    public int maxProfit(int[] prices) {
        int len = prices.length;
        if (len < 2) {
            return 0;
        }
        int[] maxProfitBefore = new int[len];
        int[] maxProfitAfter = new int[len];
        int min, max;
        
        min = max = prices[0];
        for (int i=1; i<len; ++i){
            if (prices[i] > max){
                max = prices[i];
                maxProfitBefore[i] = max - min;
            }
            else if(prices[i] < min){
                max = min = prices[i];
                maxProfitBefore[i] = maxProfitBefore[i-1];
            }
            else{
                maxProfitBefore[i] = maxProfitBefore[i-1];
            }
        }
        min = max = prices[len-1];
        for (int i=len-2; i>-1; --i){
            if (prices[i] < min){
                min = prices[i];
                maxProfitAfter[i] = max - min;
            }
            else if(prices[i] > max){
                max = min = prices[i];
                maxProfitAfter[i] = maxProfitAfter[i+1];
            }
            else{
                maxProfitAfter[i] = maxProfitAfter[i+1];
            }
        }
        int maxProfit = 0;
        int sum = 0;
        for (int i=0; i<len-1; ++i){
            sum = maxProfitBefore[i] + maxProfitAfter[i+1];
            if (maxProfit < sum) {
                maxProfit = sum;
            }
        }
        if (maxProfit < maxProfitBefore[len-1]){
            maxProfit = maxProfitBefore[len-1];
        }
        if (maxProfit < maxProfitAfter[0]){
            maxProfit = maxProfitAfter[0];
        }
        /*
        for (int i=0; i<len; ++i){
            System.out.print(maxProfitBefore[i]);
            System.out.print(" ");
        }
        System.out.println();
        for (int i=0; i<len; ++i){
            System.out.print(maxProfitAfter[i]);
            System.out.print(" ");
        }
        */
        return maxProfit;
    }
}