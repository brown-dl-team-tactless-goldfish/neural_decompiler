class Solution {
public:
    vector<string> splitMessage(string message, int limit) {
        vector<string> result;
        int n = message.size();
        int suffixLen = 3; // without digits
        int maxSegment = 0; // maxSegments for curr no of digits
        int extraDigits = 0; // Note: previous segments had one less digits and while counting available digits we need to add these extra digits
        // i.e. we can fit extra chars in 1-9 segment for segments in range 1-99
        int digit = 1;
        while(digit < 5){
            suffixLen += 2; // add new digits
            if(limit <= suffixLen)
                return result;
            maxSegment = maxSegment*10+9;
            // check if string can be fit in given digit segment length
            if(limit*maxSegment + extraDigits - suffixLen*maxSegment >= n) 
            {
                int pos = 0;
                int seg = 1;
                string suffix = "/"+ to_string(maxSegment)+ ">";
                while(pos<n) {
                    string temp = "<"+to_string(seg)+suffix;
                    int r = limit - temp.size();
                    temp = message.substr(pos,r)+ temp;
                    result.push_back(temp);
                    pos +=r;
                    ++seg;
                }
                // replace total segment with exact numbers
                string s = to_string(--seg);
                for(auto& r:result)
                    r.replace(r.size()-(digit+1),digit,s);

                return result;
            }
            extraDigits += maxSegment;
            ++digit;
        }
        return result;
    }
};