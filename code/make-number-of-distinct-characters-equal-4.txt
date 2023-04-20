class Solution {
public:
    bool isItPossible(string word1, string word2) {
        unordered_map<char,int> mp1, mp2;
        int n1=word1.size(),n2=word2.size();
        for (char c : word1) mp1[c-'a']++;
        for (char c : word2) mp2[c-'a']++;
        int ns1=mp1.size(),ns2=mp2.size();
        for(int i=0;i<26;i++){
            for(int j=0;j<26;j++){
                if(mp1.count(i) and mp2.count(j)){
                mp1[j]++;
                mp2[i]++;
                if(--mp1[i]==0)mp1.erase(i);
                if(--mp2[j]==0)mp2.erase(j);
                if(mp1.size()==mp2.size())return true;
                mp1[i]++;
                mp2[j]++;
                if(--mp1[j]==0)mp1.erase(j);
                if(--mp2[i]==0)mp2.erase(i);
                }   
            }
        }
        return false;
    
    }
};