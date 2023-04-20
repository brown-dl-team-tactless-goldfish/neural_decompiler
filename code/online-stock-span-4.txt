class StockSpanner {
public:
   stack<pair<int,int>> s;
    StockSpanner() {        
    }
    
    int next(int price) {
       int res = 1;
         while(s.size() && s.top().first<=price){
             res+= s.top().second;
             s.pop();
         }
       s.push({price,res});
       return res;
    }
};