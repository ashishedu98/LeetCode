class Solution {
public:
    bool isPalindrome(string s) {
    deque<char> q;
    for(auto x:s){
        if(isalnum(x)){
            q.push_back(toupper(x));
        }
    }
    while(!q.empty()){
        char x = q.front();
        q.pop_front();
        cout<<x;
        if(!q.empty()){
            char y = q.back();
            cout<<y;
            q.pop_back();
            if(y!=x){
                return false;
            }
        }
    }
    return true;
    }
};