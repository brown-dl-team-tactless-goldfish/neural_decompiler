int* findMinHeightTrees(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize){
    //special case, edgesSize == 0
    //>>>>
    if(edgesSize == 0){
        *returnSize = n;
        int* ans = malloc(n * sizeof(int));
        for(int i = 0; i < n; i++)
            ans[i] = i;
        return ans;
    }
    //<<<<
    
    int* vertexEdge = calloc(n , sizeof(int));
    //caculate each nodes's neighbor
    for(int i = 0; i < edgesSize; i++){
        vertexEdge[ edges[i][0] ]++;
        vertexEdge[ edges[i][1] ]++;
    }
    //map[i][x] save vertex's neighbor
    //mapIdx[i] save vertex's number of neighbor
    int** map = malloc(n * sizeof(int*));
    int* mapIdx = calloc(n, sizeof(int));
    int* queue = malloc(n * sizeof(int));
    for(int i = 0; i < n; i++){
        map[i] = malloc(vertexEdge[i] * sizeof(int));
    }
    int idx, vtx;
    //create map
    //>>>>
    for(int i = 0; i < edgesSize; i++){
        vtx = edges[i][0];
        idx = mapIdx[vtx];
        map[vtx][idx] = edges[i][1];
        mapIdx[vtx]++;
        
        vtx = edges[i][1];
        idx = mapIdx[vtx];
        map[vtx][idx] = edges[i][0];
        mapIdx[vtx]++;
    }
    //<<<<
    int qIdx = 0;
    //neighbor == 1, add into queue
    for(int i = 0; i < n; i++){
        if(vertexEdge[i] == 1){
            queue[qIdx] = i;
            qIdx++;
        }
    }

    int begin = 0, end = qIdx;
    //iterate queue
    while(qIdx < n){
        for(int i = begin; i < end; i++){
            vertexEdge[queue[i]] = 0;
            mapIdx[queue[i]] = 0;
            int dec = map[queue[i]][0] ;
            vertexEdge[dec]--;
            if(vertexEdge[dec] == 1){
            //add to queue
                queue[qIdx] = dec;
                qIdx++;
            }
            for(int j = 0; j < mapIdx[dec]; j++){
                if(map[dec][j] == queue[i]){
                //delete from map
                    map[dec][j] = map[dec][mapIdx[dec]-1];
                    break;
                }
            }
            mapIdx[dec]--;
        }
        begin = end;
        end = qIdx;
    }

    *returnSize = end - begin;
    int* ans = malloc((*returnSize ) * sizeof(int));
    for(int i = 0; i < (*returnSize ); i++){
        ans[i] = queue[begin];
        begin++;
    }
    return ans;
}