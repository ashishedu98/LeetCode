class Solution {
public:
    int maxProfit(vector<int>& prices) {
        ios_base::sync_with_stdio(false);
        int profit=0;
        int lowest=prices[0];
        for(auto price:prices){
            if(price<lowest){
                lowest = price;
            }
            profit = max(profit, price-lowest);
        }
        return profit;
    }
};