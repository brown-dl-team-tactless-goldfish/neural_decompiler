class Solution {
public:
    string longestSubsequenceRepeatedK(string s, int k) {
        int freq[26]={};
        for(auto& ch:s)
            freq[ch-'a']++;
        int len=0;
        for(int i=0;i<26;++i)
            len+=freq[i]/=k;
        for(;len>0;--len){
            string ss;
            if(generate(len,freq,ss,s,k))
                return ss;
        }
        return "";
    }
private:
    bool generate(int n, int* freq, string& ss, string& s, int k) {
        if(n==0)
            return isSubsequence(s,ss,k);
        for(int i=25;i>=0;--i){ //lexicographically largest one first
            if(freq[i]==0)
                continue;
            ss+='a'+i;
            freq[i]--;
            if(generate(n-1,freq,ss,s,k))
                return true;
            freq[i]++;
            ss.pop_back();
        }
        return false;
    }
    bool isSubsequence(string& s, string& t, int k) {
        for(int is=0,it=0,sleft=s.length(),tleft=k*t.length();k>0 && sleft>=tleft;++is,--sleft){
            if(s[is]==t[it])
                it++,tleft--;
            if(it==t.length())
                it=0,k--;
        }
        return k==0;
    }
};