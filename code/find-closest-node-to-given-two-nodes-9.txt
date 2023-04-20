class Solution {
public:
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        
        
        vector<int>visited1(edges.size() , -1);
        vector<int>visited2(edges.size() , -1);
        
      if(node1 == node2){
          return node1;
      }
        

        
        int p = node1 ,q = node2;
        int m = 1 , n = 1;
        visited1[p] = 0;
        while(edges[node1] != -1 && visited1[edges[node1]] == -1){
           int x =  edges[node1];
            visited1[x] = m;
            node1 = x;
            m++; 
          
        }
   
        visited2[q] = 0;
        while(edges[node2] != -1 && visited2[edges[node2]] == -1){
            int x = edges[node2];
            visited2[x] = n;
            node2 = x;
            n++;
        }
        
 
        int c = INT_MAX;
        
        int index = -1;
        for(int i = 0 ; i < edges.size() ; i++){
            
            if(visited2[i] != -1 && visited1[i] != -1){
                  int p = max(visited1[i] , visited2[i]);
                 if(c > p ||( c == p && i < index ) ){
                     index = i;
                     c = p;
                 }
            }
        }
        return index;
        
    }
};