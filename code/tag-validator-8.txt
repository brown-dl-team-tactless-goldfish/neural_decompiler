class Solution {
public:
    bool isValid(string code) {
        stack<string> tag;
        int i = 0, ind;
        string curtag;
        bool interp = true;
        while (i<code.size()){
            if (interp && code[i]=='<'){
                if (i+1<code.size() && code[i+1]=='/'){
                    ind = code.find('>', i+1);
                    if (ind==string::npos) return false;
                    curtag = code.substr(i+2, ind-i-2);
                    if (tag.empty() || tag.top()!=curtag) return false;
                    tag.pop();
                    i = ind+1;
                }else if (i+1<code.size() && code[i+1]=='!'){
                    if (tag.empty() || code.substr(i,9)!="<![CDATA[") return false;
                    interp = false;
                    i += 9;
                }else {
                    ind = code.find('>', i+1);
                    if ((tag.empty() && i>0) || ind==string::npos || ind==i+1 || ind > i+10) return false;
                    curtag = code.substr(i+1, ind-i-1);
                    for (char c:curtag){
                        if (c<'A' || c>'Z') return false;
                    }
                    tag.push(curtag);
                    i = ind+1;
                }
                
            }else if (!interp && code[i]==']'){
                if (tag.empty()) return false;
                else if (code.substr(i, 3)=="]]>"){
                    interp = true; i+=3; 
                }else{
                    i++;
                }
            }else if (tag.empty()){
                return false;
            }else{
                i++;
            }
        }
        return tag.empty();
    }
};