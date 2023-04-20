class Solution {
public:
    Solution(){
        vector<int> tmp(4,0);
        perfect_rect = tmp;
    }
    bool isRectangleCover(vector<vector<int>>& rectangles) {
        int minsum(INT_MAX),maxsum(INT_MIN);
        int subrectarea = 0;
        
        for(vector<int> rect : rectangles){
            subrectarea += area(rect);
            if(rect[0]+rect[1] < minsum){
                perfect_rect[0] = rect[0];
                perfect_rect[1] = rect[1];
                minsum = rect[0]+rect[1];
            }
            if(rect[2]+rect[3] > maxsum){
                perfect_rect[2] = rect[2];
                perfect_rect[3] = rect[3];
                maxsum = rect[2]+rect[3];
            }
        }
        if(subrectarea != area(perfect_rect))
            return false;
         
        for(vector<int> rect : rectangles){
            VertexPos E;
            E = getVertexPos(rect[0],rect[1]);
            if(!checkVertexinMap(rect[0],rect[1],E))
                return false;
            E = getVertexPos(rect[2],rect[1]);
            if(!checkVertexinMap(rect[2],rect[1],E))
                return false;
            E = getVertexPos(rect[0],rect[3]);
            if(!checkVertexinMap(rect[0],rect[3],E))
                return false;
            E = getVertexPos(rect[2],rect[3]);
            if(!checkVertexinMap(rect[2],rect[3],E))
                return false;
        }
        
        for(auto it=EdgeMap.begin(); it!=EdgeMap.end(); it++)
            if(it->second != 2)
                return false;
        
        for(auto it=InsideMap.begin(); it!=InsideMap.end(); it++)
            if(it->second != 2 && it->second != 4)
                return false;

        return true;
    }
    
private:
    vector<int> perfect_rect;
    enum VertexPos{Corner,Edge,Inside};
    unordered_map<string,int> CornerMap; // all values should be 1
    unordered_map<string,int> EdgeMap;   // all values should be 2
    unordered_map<string,int> InsideMap; // all values should be 2 or 4
    
    
    bool checkVertexinMap(int x, int y, VertexPos v){
        string s = to_string(x) + " " + to_string(y);
        if(v == Corner){
            CornerMap[s]++;
            if(CornerMap[s]>1)
                return false;
        }
        else if(v == Edge){
            EdgeMap[s]++;
            if(EdgeMap[s]>2)
                return false;
        }
        else{
            InsideMap[s]++;
            if(InsideMap[s]>4)
                return false;
        }
        return true;
    }
    
    //get the vertex position
    VertexPos getVertexPos(int x, int y){
        int num = 0;
        if(x ==perfect_rect[0] || x == perfect_rect[2])
            num++;
        if(y == perfect_rect[1] || y == perfect_rect[3])
            num++;
        if(num==0)
            return Inside;
        else if(num==1)
            return Edge;
        return Corner;
    }
    
    int area(const vector<int>& rect){
        return (rect[2]-rect[0])*(rect[3]-rect[1]);
    }
};