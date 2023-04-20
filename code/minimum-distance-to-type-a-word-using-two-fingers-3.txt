class Solution {
private:
    vector<vector<vector<int>>>mem;
    int distance(char a, char b) {
        int x1 = (a-'A') / 6, y1 = (a-'A') % 6;
        int x2 = (b-'A') / 6, y2 = (b-'A') % 6; 
        return abs(x1-x2) + abs(y1-y2);
    }
    int solve(string &word,int index,char first,char second){
        int n=word.size();
        int firstPos=first-'A',secondPos=second-'A';
        if(index==n){
            return 0;
        } else if(mem[index][firstPos][secondPos]!=-1){
            return mem[index][firstPos][secondPos];
        } else {
            int ans1=distance(word[index],first)+solve(word,index+1,word[index],second);
            int ans2=distance(word[index],second)+solve(word,index+1,first,word[index]);
            return mem[index][firstPos][secondPos]=min(ans1,ans2);
        }
    }
public:
    int minimumDistance(string word) {
        int n=word.size();
        mem=vector<vector<vector<int>>>(n,vector<vector<int>>(26,vector<int>(26,-1)));
        int ans=INT_MAX;
        for(char c='A';c<='Z';c++){
            ans=min(ans,solve(word,0,word[0],c));
        }
        return ans;
    }
};