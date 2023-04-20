class Solution {
public:
int sumSubarrayMins(vector<int>& arr) {
    stack<pair<int,int>> s1; //for left fill
    stack<pair<int,int>> s2; // for right fill
    vector<long> left(arr.size());
    vector<long> right(arr.size());
    for(int i=0;i<arr.size();++i){
                int c=1;
                while(!s1.empty() && s1.top().first >= arr[i]){
                 c+=s1.top().second;
                s1.pop();
                }
                s1.push({arr[i],c});
                left[i] = c;
        }
    
     for(int i=arr.size()-1;i>=0;i--){
         int c=1;
                while(!s2.empty() && s2.top().first > arr[i]){
                 c+=s2.top().second;
                s2.pop();
                }
                s2.push({arr[i],c});
                right[i] = c;
    }
    long int sum=0;
    for(int i=0;i<arr.size();++i){
        long int c = arr[i];
        sum+=(c*left[i]*right[i]);
             sum=sum % (1000000000 + 7);

    }
    return sum;
}
};