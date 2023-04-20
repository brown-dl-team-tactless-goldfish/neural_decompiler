void right(int i, int j, int** list, int* count){
    int copy[200];
    int Count = 0;
    int a = 0;
    int b = 0;
    while (a < count[j] || b < count[j+1]){
        if (a >= count[j]){
            while (b < count[j+1]){
                copy[Count] = list[j+1][b];
                Count++;
                b++;
            }
        } else if (b >= count[j+1]){
            while (a < count[j]){
                copy[Count] = list[j][a];
                Count++;
                a++;
            }
        } else if (list[j][a] > list[j+1][b]){
            copy[Count] = list[j+1][b];
            Count++;
            b++;
        } else if (list[j][a] < list[j+1][b]){
            copy[Count] = list[j][a];
            Count++;
            a++;
        } else {
            copy[Count] = list[j][a];
            Count++;
            a++;
            b++;
        }
    }
    while (Count > 0 && copy[Count-1] > 99){
        Count--;
    }
    for (int i = 0 ; i < Count ; i++){
        list[j][i] = copy[i]+1;
    }
    count[j] = Count;
}

void left(int i, int j, int** list, int* count){
    int copy[200];
    int Count = 0;
    int a = 0;
    int b = 0;
    while (a < count[j] || b < count[j+1]){
        if (a >= count[j]){
            while (b < count[j+1]){
                copy[Count] = list[j+1][b];
                Count++;
                b++;
            }
        } else if (b >= count[j+1]){
            while (a < count[j]){
                copy[Count] = list[j][a];
                Count++;
                a++;
            }
        } else if (list[j][a] > list[j+1][b]){
            copy[Count] = list[j+1][b];
            Count++;
            b++;
        } else if (list[j][a] < list[j+1][b]){
            copy[Count] = list[j][a];
            Count++;
            a++;
        } else {
            copy[Count] = list[j][a];
            Count++;
            a++;
            b++;
        }
    }
    int h = 0;
    while (h < Count && copy[h] < 1){
        h++;
    }
    count[j] = 0;
    for (; h < Count ; h++){
        list[j][count[j]] = copy[h]-1;
        count[j]++;
    }
}

bool hasValidPath(char** grid, int gridSize, int* gridColSize){
    int x = gridSize-1;
    int y = *gridColSize-1;
    if (grid[x][y] == '(' || grid[0][0] == ')'  || (x+y) % 2 == 0){
        return false;
    }
    
    int** list = malloc(sizeof(int*)*(*gridColSize));
    for (int i = 0 ; i < (*gridColSize) ; i++){
        list[i] = malloc(sizeof(int)*100);
    }
    int* count = calloc(101,sizeof(int));
    list[y][0] = 1;
    count[y]++;
    
    for (int j = y-1 ; j >= 0 ; j--){
        if (list[j+1][0] >= 0){
            if (grid[x][j] == ')'){
                list[j][0] = list[j+1][0]+1;
                count[j]++;
            } else {
                list[j][0] = list[j+1][0]-1;
                if (list[j][count[j]] >= 0){
                    count[j]++;
                }
            }
        } else {
            list[j][0] = -1;
        }
    }
    
    for (int i = x-1 ; i >= 0 ; i--){
        if (list[y][0] >= 0){
            if (grid[i][y] == ')'){
                list[y][0]++;
            } else {
                list[y][0]--;
                if (list[y][0] < 0){
                    count[y]--;
                }
            }
        }
        for (int j = y-1 ; j >= 0 ; j--){
            if (grid[i][j] == ')'){
                right( i, j, list, count);
            } else {
                left( i, j, list, count);
            }
        }
    }
    int ans = list[0][0];
    for (int i = 0 ; i < *gridColSize ; i++){
        free(list[i]);
    }
    free(list);
    return ans == 0 ? true : false;
}