  vector<int> missingRolls(vector<int>& a, int mean, int n) {
        vector<int> resvec;
        int suma = accumulate(a.begin(), a.end(), 0);
        int actSum = mean * (a.size()+n);
        int sumOfRemVal = actSum - suma;
        // cout << "SUM: " << sumOfRemVal << endl;
        
        int val = sumOfRemVal/n;
        int rem=  sumOfRemVal % n;
        if(val==0 || val > 6 || val < 0 || (val==6 &&rem>0)) return resvec;

        while(n--){
            resvec.push_back(val);
        }
        int i=0;
        while(rem){
            resvec[i]+=1;
            i+=1;
            rem--;
        }
        return resvec;
    }