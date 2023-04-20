class Solution {
public:
    int minimumDeletions(string s) 
    {
        int as = 0, bs = 0;
        for( const char& c : s )
            if( c == 'a' )
                ++as;
        
        int del = as;
        for( const char& c : s )
        {
            if( c == 'b' )
                ++bs;
            else
                --as;
            
            del = min( del, (as+bs) );
        }
        return del;
    }
};