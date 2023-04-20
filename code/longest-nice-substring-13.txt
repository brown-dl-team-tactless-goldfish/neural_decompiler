class Solution {
public:

   bool isNice(string h){

		for(int i=0; i<h.length(); i++){

			char c = h[i];
			if(c >= 65 && c <=90){
				c = c + 32;
			}
			else{
				c = c - 32;
			}
			if(h.find(c) == string ::npos){
				return false;
			}
		}
		return true;
	}


	string longestNiceSubstring(string s) {

		string res= "";
		int n = s.size();

		for(int i=0; i<n; i++)
		{
			string t="";
			t += s[i];

			for(int j = i+1; j<n; j++)
			{
				t += s[j];
				if(isNice(t)  && t.length()> res.length())
					res = t;
			}
		}
		return res;
	}
};