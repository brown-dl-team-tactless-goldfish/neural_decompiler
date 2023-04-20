bool checkIfExist(int* arr, int arrSize){
    int* hash = (int*)calloc(2001, sizeof(int));/* -1000 - 0 - 1000 */
    int curr, process;
    for(int i = 0; i < arrSize; i++)
    {
        curr = arr[i];
        
        if(curr & 1) /* odd */
        {
            process = curr * 2;
            if((process <= 1000) && (process >= -1000) && hash[1000+process])
                return true;
        }
        else /* even */
        {
            process = curr * 2;
            if((process <= 1000) && (process >= -1000) && hash[1000+process])
                return true;
            process = curr / 2;
            if(hash[1000+process])
                return true;
        }
        hash[1000+curr]++;
    }
    return false;
}