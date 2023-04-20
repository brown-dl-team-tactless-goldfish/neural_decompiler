class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int len = speed.size();
        vector<double> estArrivalTimeToDest;
        map<int, int> indexPosMap;
        for (int i = 0; i < len; i++) {
            indexPosMap[position[i]] = i;
        }
        
        for (auto &it : indexPosMap) {
            int realIdx = it.second;
            int distToDest = target - position[realIdx];
            double estArrivalTime = distToDest * 1.0 / speed[realIdx] * 1.0;
            estArrivalTimeToDest.push_back(estArrivalTime);
        }
        
        stack<double> monoDecStack;
        for (int i = 0; i < len; i++) {
            while (!monoDecStack.empty() && estArrivalTimeToDest[i] >= monoDecStack.top()) {
                monoDecStack.pop();
            }
            monoDecStack.push(estArrivalTimeToDest[i]);
        }
        
        return monoDecStack.size();
    }
};