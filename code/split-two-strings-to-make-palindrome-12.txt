class Solution {
public:
    int n;
    bool isPalindrome(string s,int i,int j) {
        while (i < j && s[i] == s[j])
            i++, j--;
        return i >= j;
    }
    bool checkPalindrome(string a, string b){
        int i=0,j=a.size()-1;
        while(i<j && a[i]==b[j])
            i++,j--;
        return isPalindrome(a,i,j) || isPalindrome(b,i,j);
    }
    bool checkPalindromeFormation(string a, string b) {
        return checkPalindrome(a,b) ||checkPalindrome(b,a);
    }
};