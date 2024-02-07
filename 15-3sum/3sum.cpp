class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>>ans;
        vector<vector<int>>returnAns;
        int n = nums.size();
        sort(nums.begin(),nums.end());
        for(int i=0;i<n-1;i++){
            int x = nums[i];
            int start = i+1;
            int end = n-1;
            int sum = 0;
            while(start<end){
                sum=nums[start]+nums[end];
                if(sum+x==0){
                    vector<int>res = {nums[i],nums[start],nums[end]};
                    ans.insert(res);
                    start++;
                }
                else if(sum<(-x)){
                    start++;
                }
                else{
                    end--;
                }
            }
        }
        for(auto a:ans){
            returnAns.push_back(a);
        }
        return returnAns;
    }
};