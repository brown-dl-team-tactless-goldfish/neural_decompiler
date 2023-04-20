class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        int res = 0;
        int len = arr.size();
        for(int i = 0; i < len-1; i++){
            int left = 0, right = 1, mi_left, mi_right, mi = INFINITY;
            while(right < len){
                if(arr[left] == -1){
                    left = right;
                    right++;
                }else if(arr[right] == -1){
                    right++;
                }else{
                    if(mi > arr[left]*arr[right]){
                        mi_left = left;
                        mi_right = right;
                        mi = arr[left]*arr[right];
                    }
                    left = right;
                    right++;
                }
            }
            res += mi;
            if(arr[mi_left] > arr[mi_right]) arr[mi_right] = -1;
            else arr[mi_left] = -1;
        }
        return res;        
    }
};