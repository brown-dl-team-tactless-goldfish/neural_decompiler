class Solution {
public int collectTheCoins(int[] coins, int[][] edges) {

    int n = edges.length;
    ArrayList<HashSet<Integer>> list = new ArrayList<>();
    Queue<Integer> q = new LinkedList<>();
    int totalEdges = 2*n;
    int deletedEdges = 0;

    for(int i=0;i<=n;i++){
        list.add(new HashSet<Integer>());
    }

    for(int i=0;i<n;i++){
        int a = edges[i][0];
        int b = edges[i][1];
        list.get(a).add(b);
        list.get(b).add(a);
    }

    for(int i=0;i<=n;i++){
        if(list.get(i).size()==1 && coins[i]==0){
            q.add(i);
        }
    }
    while(!q.isEmpty()){
        int cur = q.remove();
        if(list.get(cur).size()==0) continue;
        int p = list.get(cur).iterator().next();
        list.get(cur).remove(p);
        list.get(p).remove(cur);
        if(list.get(p).size()==1 && coins[p]==0){
            q.add(p);
        }
        deletedEdges += 2;
    }

    for(int i=0;i<=n;i++){
        if(list.get(i).size()==1){
            q.add(i);
        }
    }

    int size=2;
    while(size>0){
        size--;
        int qsize = q.size();
        while(qsize>0){
            qsize--;
            int cur = q.remove();
            if(list.get(cur).size()==0) continue;
            int p = list.get(cur).iterator().next();
            list.get(cur).remove(p);
            list.get(p).remove(cur);
            if(list.get(p).size()==1){
                q.add(p);
            }
            deletedEdges += 2;
        }
    }

    return totalEdges - deletedEdges;
}
}