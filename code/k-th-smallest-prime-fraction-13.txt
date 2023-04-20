vector <int> v(2);
int a=1; 

class Solution {
public:
    
    void is_valid(vector<int>& arr,int k,double mid)
    {
        int n=arr.size();
        int count=0;
        int num=-1,den=-1;
        double imax = INT_MIN;
        for(int i=0;i<n;i++)
        {
            for(int j=n-1;j>i;j--)
            {
                double val = (double)arr[i]/arr[j];
                
                if( val < mid )
                {
                    count++;
                    if(imax <= val)
                    {
                        imax = val;
                        num = arr[i];
                        den = arr[j];
                    }
                }
                    
            }
        }
        
        if(count>k)
        a = -1;
        
        else if(count<k)
        a = 0;
        
        else
        {
            v[0] = num;
            v[1] = den;
        }
    }
    
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        
        int n = arr.size();
        double low = arr[0]/arr[n-1];
        double high = 1;
        double mid;
       
        
        while(low<high)
        {
            mid = low + (high-low)/2;
            a=1;
            is_valid(arr,k,mid);
            
            if(a==0)
            low = mid;
            
            else if(a==-1)
            high = mid;
            
            else
                break;
        }
        return v;
    }
};