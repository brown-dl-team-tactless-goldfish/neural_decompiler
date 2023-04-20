class Solution {
public:
    int latestTimeCatchTheBus(vector<int>& buses, vector<int>& passengers, int capacity) {
        sort(buses.begin() , buses.end());
        vector<int> pass = passengers;
        sort(pass.begin() , pass.end());
        
        vector<int> a; int j=0;
        
        for(int i=0 ; i<buses.size()-1 ; i++)
        {
            int count=0;
            while(j<pass.size() && count<capacity && pass[j]<=buses[i]) 
            {
                a.push_back(pass[j]);
                count++;
                j++;
            }
        }
        
        int count=0;
        
        while(j<pass.size() && count<capacity && pass[j]<=buses[buses.size()-1])
        {
            a.push_back(pass[j]);
            count++;
            j++;
            
        }
        
        if(count == capacity)
        {
            int m = a.size()-1;
            
            while(m>0)
            {
                if(a[m] == a[m-1]+1) m--;
                else return a[m]-1;
            }
            return a[0]-1;
        }
        else{
            int m = a.size()-1;
            int last = buses[buses.size()-1];
            
            while(m>=0){
                if(a[m] == last) last--, m-- ;
                else return last;
            }
            return last;
        }
    }
};