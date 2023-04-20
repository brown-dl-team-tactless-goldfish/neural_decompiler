bool validPath(int n, int** edges, int edgesSize, int* edgesColSize, int source, int destination){
    if (source == destination) return true;
    
    bool visited_map[n], stk_map[n];
    for (int i = 0; i < n; i++){
        stk_map[i] = false;     // To record element(s) we had in stack
        visited_map[i] = false; // To record vertex(es) we had visited
    } 
    int stk[n];
    unsigned int pt = -1;
    stk[++pt] = source;     // push source to stack
    stk_map[source] = true; // record in stack map

    while (pt != -1){
        while (visited_map[stk[pt]] == true) pt--; // pop while the vertex in the stack is visited
        visited_map[stk[pt]] = true;
        int top = stk[pt--];    // pop the top element of the stack and take its value
        stk_map[top] = false;   // since we popped the element, it's not in stack anymore

        /* We start to traverse through the "edges" 2D array, 
        finding adjacent vertex(es) of the "top" vertex.*/
        for(int i = 0; i < edgesSize; i++){
            for(int j = 0; j < *edgesColSize; j++){
                if (edges[i][j] == top){    
                    int vertex = edges[i][*edgesColSize-1-j];
                    if (vertex == destination) return true;
                    if (visited_map[vertex] == false && stk_map[vertex] == false){
                        /* if the adjacent vertex is not visited and not in stack, 
                        push the adjacent vertex to stack.*/
                        stk[++pt] = vertex; 
                        stk_map[vertex] = true;
                    } 
                    edges[i][j] = n;                // change the used edges into invalid number
                    edges[i][*edgesColSize-1-j] = n;
                    break;
                }
            }
        } 
    }
    return visited_map[destination];
}