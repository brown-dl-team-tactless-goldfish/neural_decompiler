class Solution {
public:
    int poorPigs(int buckets, int mtd, int mtt) {
        if(buckets == 1) return 0;
        int ans = 1;
        for(int p=1; pow((mtt / mtd) + 1, p) < buckets; p++) ans++;
        return ans;
    }
};