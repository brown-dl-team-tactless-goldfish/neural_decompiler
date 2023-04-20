class Solution {
private:
    void evalfrac(int& a, int& b, int c, int d, char op) {
        // single step evaluation
        // a/b + c/d = (ad+bc)/bd
        // a/b - c/d = (ad-bc)/bd
        const int nu = (op == '+' ? a*d + b*c : a*d - b*c);
        const int deno = b*d;
        // reduce
        const int tmp = gcd(deno, nu);
        a = nu / tmp;
        b = deno / tmp;
    }
public:
    string fractionAddition(string expression) {
        int rstnu = 0, rstdeno = 1; // for resulting numerator & denominator
        char op = '+'; // current operator
        // loop the expression
		int pos = 0; 
        while (pos < expression.size()) {
            if (isdigit(expression[pos])) {
                // extract a fraction number nu/deno
                int nu = 0;
                int deno = 0;
                while (isdigit(expression[pos])) {
                    nu = nu * 10 + (expression[pos] - '0');
                    pos += 1;
                }
                pos += 1;
                while (isdigit(expression[pos])) {
                    deno = deno * 10 + (expression[pos] - '0');
                    pos += 1;
                }
                // evaluate & update rstnu/rstdeno
                evalfrac(rstnu, rstdeno, nu, deno, op);
            }
            else {
                // extract an opeartor
                op = expression[pos];
                pos += 1;
            }
        }
        // generate rst string
        string rst = to_string(rstnu) + '/' + to_string(rstdeno);
        return rst;
    }
};