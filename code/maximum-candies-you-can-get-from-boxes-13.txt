class Solution {
public:
    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes, vector<int>& initialBoxes) 
    {
        queue<int> q;
        int result=0;
        vector<bool> reachableClosedBoxes(status.size(),false);  //Only used to store boxes that are reached but closed.
        for(int &i:initialBoxes)            //Push initial boxes that we can open in the queue.
            if(status[i])
                q.push(i);
            else
                reachableClosedBoxes[i]=true;
        while(!q.empty())                   //Continue until no more boxes are left that can be opened.
        {
            result+=candies[q.front()];			//Add candies we got.
            for(int &i:keys[q.front()])				//Open the box whose keys are found.
            {
                if(!status[i]&&reachableClosedBoxes[i])//If the box was previously closed and we already reached it,use it as an open box
                    q.push(i);
                status[i]=1;
            }
            for(int &i:containedBoxes[q.front()])		//Push all the boxes within this box for then next cycle in the queue.
                if(status[i])
                    q.push(i);
                else
                    reachableClosedBoxes[i]=true;      //The box is closed, wait until we get the keys for this box.
            q.pop();
        }
        return result;
    }
};