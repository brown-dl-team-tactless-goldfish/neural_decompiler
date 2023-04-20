// sort end
int cmpfunc( const void** p1,  const void** p2){
   int* arr1 = *(int**)p1;
   int* arr2 = *(int**)p2;
  if(arr1[1] == arr2[1]){
      if(arr1[0] == arr2[0])
          return 0;
      else if(arr1[0] > arr2[0])
          return 1;
      else 
          return -1;      
  } 
  else{
      if(arr1[1] == arr2[1])
          return 0;
      else if(arr1[1] > arr2[1])
          return 1;
      else 
          return -1;
  }  
}

int findMinArrowShots(int** points, int pointsSize, int* pointsColSize){
    int i;
    qsort(points, pointsSize, sizeof(int*), cmpfunc);
    int k = points[0][1];
    int cn = 1;
    for(i = 1; i < pointsSize; i++){
        if(points[i][0] > k){
            cn++;
            k = points[i][1];
        }    
    }
    
    return cn;
}