#define M 1000000007
class Solution {
public:
    int numOfWays(int n) {
        unsigned long long int c2 = 6;
        unsigned long long int c3 = 6;
        unsigned long long int tmp = 0;
        for(int i=2;i<=n;++i){
            tmp = c3;
            c3 = (2*c3)%M + (2*c2)%M;
            c2 = (2*tmp)%M + (3*c2)%M;
            c3 = c3%M;
            c2 = c2%M;
        }
        return (c3%M+c2%M)%M;
    }
};
/*
    2 cases:
    2 colors    |               3 colors

        A B A                   A B C
    2c       3c             2C        3C
C A C       B A C        C A C      B A C
B A B       C A B        B A B      C A B
B C B

so from this equation becomes:
c2 = 3*c2 + 2*c3
c3 = 2*c2 + 2*c3
c2 at starting = 6;
c3 at starting = 6; 
*/