class Solution {
public:
    NestedInteger deserialize(string s) {
        int index = 0;
        char c = s[index];
        if (c == '[') {
            return parseList(s, index);
        } else {
            // starts with 0-9, '-'
            return parseNumber(s, index);
        }
    }
    
    NestedInteger parseList(string &s, int &index) {
        index++; // eat '['
        NestedInteger root;
        while (index < s.size()) {
            char c = s[index];
            if (c == '[') {
                root.add(parseList(s, index));
            } else if (isNumber(c) || c == '-') {
                root.add(parseNumber(s, index));
            } else if (c == ',') {
                // skip
                index++;
            } else if (c == ']') {
                break;
            }
        }
        index++; // eat ']'
        return root;
    }
    
    NestedInteger parseNumber(string &s, int &index) {
        int n = 0;
        int positive = 1;  // flag for positive number
        if (s[index] == '-') {
            positive = -1;
            index++;
        }
        while (index < s.size()) {
            char c = s[index];
            if (isNumber(c)) {
                n = 10 * n + c - '0';
                index++;
            } else {
                break;
            }
        }
        return NestedInteger(n * positive);
    }
    
    bool isNumber(char c) {
        return '0' <= c && c <= '9';
    }
};