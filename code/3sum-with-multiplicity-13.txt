class Solution {
public:
    int m = 1e9+7;
    int threeSumMulti(vector<int>& arr, int target) {
        sort(arr.begin(), arr.end());
        set<vector<int>> st;
        unordered_map<int,int> mp;
        for(auto x: arr){
            mp[x]++;
        }
        getTriplets(st, arr, target);
        // for(auto x: st){
        //     cout<< x[0]<<" "<<x[1]<<" "<<x[2]<<endl;
        // }
        int ans = 0;
        for(auto x: st){
            int a = x[0];
            int b = x[1];
            int c = x[2];
            int temp;
            if(a==b and b==c ){
                temp = multiply(mp[a], mp[a]-1, mp[a]-2);
                
            }
            else if(a==b or b==c or a==c){
                if(a==b){
                    temp = multiply2(mp[a], mp[a]-1, mp[c]);
                    
                }
                else if(b==c){
                    temp = multiply2(mp[b], mp[b]-1, mp[a]);
                    
                }
                else{
                    temp = multiply2(mp[a], mp[a]-1, mp[b]);
                    
                }
            }
            else{
                temp = multiply3(mp[a], mp[b], mp[c]);
            }
            
            ans+=temp;
            ans%=m;
        }
        return ans;
    }
    
    void getTriplets(set<vector<int>> &st, vector<int> &arr, int target){
        int i = 0,j = 1,k = 2;
        int n = arr.size();
        while(i<=n-3){
            int val = arr[i];
            int newTarget = target - val;
            j = i+1;
            k = n-1;
            while(j<k){
                if(arr[k]+arr[j]==newTarget){
                    
                    st.insert({arr[i],arr[j],arr[k]});
                    skip_j(j, arr);
                    skip_k(k, arr);
                }
                else if(arr[k]+arr[j]<newTarget){
                    skip_j(j, arr);
                }
                else{
                    skip_k(k, arr);
                }
            }
            skip_j(i, arr);
        }
            
        
        
    }
    void skip_j(int &j, vector<int> &arr){
        int val = arr[j];
        int n = arr.size();
        while(j<n and arr[j]==val)j++;
    }
    void skip_k(int &k, vector<int> &arr){
        int val = arr[k];
        while(k>=0 and arr[k]==val)k--;
    }
    int multiply(int a, int b, int c){
        long long int x = a, y = b, z = c;
        
        return ((x*y*z)/6)%m;
    }
    int multiply2(int a, int b, int c){
        long long int x = a, y = b, z = c;
        
        return ((x*y*z)/2)%m;
    }int multiply3(int a, int b, int c){
        long long int x = a, y = b, z = c;
        
        return ((x*y*z))%m;
    }
    
   
};