class Solution {
public:
    vector<long long> kthPalindrome(vector<int>& queries, int intLength) {
        vector<long long >ans;
        int val=(intLength-1)/2;
        long long  value=9*pow(10,val);
        
        for(int i=0;i<queries.size();i++){
            if(queries[i]>value){
                ans.push_back(-1);
            }
            else{
                if(intLength%2){
                    int cur=queries[i]-1;
                    
                    string s="";
                    for(int j=0;j<intLength;j++){
                        s+='0';
                    }
                    
                    for(int j=(intLength)/2;j>=0;j--){
                        int data=cur%10;
                        cur=cur/10;
                        if(j==0){
                            s[j]=1+data+'0';
                            s[intLength-1-j]=1+data+'0';
                        }
                        else{
                            s[j]=data+'0';
                            s[intLength-1-j]=data+'0';
                        }
                    }
                    // cout<<s<<endl;
                    ans.push_back(stoll(s));
                }
                else{
                    int cur=queries[i]-1;
                    
                    string s="";
                    for(int j=0;j<intLength;j++){
                        s+='0';
                    }
                    
                    for(int j=(intLength-1)/2;j>=0;j--){
                        int data=cur%10;
                        cur=cur/10;
                        if(j==0){
                            s[j]=1+data+'0';
                            s[intLength-1-j]=1+data+'0';
                        }
                        else{
                            s[j]=data+'0';
                            s[intLength-1-j]=data+'0';
                        }
                    }
                    // cout<<s<<endl;
                    ans.push_back(stoll(s));
                }
                
            }
        }
        return ans ;
    }
};