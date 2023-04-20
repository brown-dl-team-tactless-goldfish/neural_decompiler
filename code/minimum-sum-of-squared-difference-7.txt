class Solution {
  public long minSumSquareDiff(int[] nums1, int[] nums2, int k1, int k2) {
    HashMap<Long, Integer> table = new HashMap<Long, Integer>();
    for(int i = 0; i != nums1.length; i++){
      long dif = Math.abs((long)nums1[i] - nums2[i]);
      if(dif != 0)
        if(table.containsKey(dif)) table.put(dif, table.get(dif) + 1);
        else table.put(dif, 1);
    }
      
    int k = k1 + k2, id = 1;
    long ans = 0;
    long t[][] = new long[table.size()+1][2];
    for(Map.Entry<Long, Integer> it : table.entrySet()){
      t[id][0] = it.getKey();
      t[id++][1] = it.getValue();
    }
    Arrays.sort(t, Comparator.comparingLong(o -> o[0]));
    
    id = table.size();
    while(id != 0 && k != 0){
      long dif = (t[id][0] - t[id-1][0]) * t[id][1];                  
      if(dif <= k){
        id--;
        t[id][1] += t[id+1][1];
        k -= dif;
      }
      else{
        long n = t[id][0] - k/t[id][1]; 
        ans += n * n * (t[id][1] - k%t[id][1]) + (n-1) * (n-1) * (k%t[id][1]); 
        id--;
        break;
      }
    }
      
    for(; id >= 0; id--) ans += t[id][0] * t[id][0] * t[id][1];
    return ans;      
  }
}